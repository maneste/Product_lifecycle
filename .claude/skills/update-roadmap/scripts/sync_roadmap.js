#!/usr/bin/env node
/**
 * sync_roadmap.js
 * Syncs ROADMAP.md checkbox states based on file existence and frontmatter status.
 *
 * Checkbox convention:
 *   [ ] — file does not exist
 *   [-] — file exists (status: draft, or has content but no frontmatter)
 *   [x] — file exists with status: done in YAML frontmatter
 *
 * Usage:
 *   node sync_roadmap.js [--roadmap <path>] [--root <repo-root>] [--dry-run]
 *
 * Defaults:
 *   --roadmap  ROADMAP.md (relative to repo root)
 *   --root     cwd
 */

const fs = require('fs');
const path = require('path');

// --- CLI args ---
const args = process.argv.slice(2);
const getArg = (flag) => {
  const i = args.indexOf(flag);
  return i !== -1 ? args[i + 1] : null;
};
const dryRun = args.includes('--dry-run');
const repoRoot = getArg('--root') || process.cwd();
const roadmapRelPath = getArg('--roadmap') || 'ROADMAP.md';
const roadmapPath = path.resolve(repoRoot, roadmapRelPath);

// --- Helpers ---
function readFrontmatterStatus(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^---\s*\n([\s\S]*?)\n---/);
  if (match) {
    const statusMatch = match[1].match(/^status:\s*(.+)$/m);
    if (statusMatch) return statusMatch[1].trim();
  }
  // No frontmatter — return 'draft' if file has non-trivial content
  return content.trim().length > 0 ? 'draft' : 'placeholder';
}

function computeCheckbox(filePath) {
  const absPath = path.resolve(repoRoot, filePath);
  if (!fs.existsSync(absPath)) return ' ';
  const status = readFrontmatterStatus(absPath);
  if (status === 'done') return 'x';
  if (status === 'placeholder') return ' ';
  return '-'; // draft or any other value
}

// Matches lines like: - [ ] Foo — `path/to/file.md`
//                     - [-] Foo — `path/to/file.md`
//                     - [x] Foo — `path/to/file.md`
const TASK_LINE_RE = /^(\s*-\s*\[)([x \-])(\]\s+.+?—\s+`)([^`]+)(`)/;

// --- Main ---
if (!fs.existsSync(roadmapPath)) {
  console.error(`Error: ROADMAP.md not found at ${roadmapPath}`);
  process.exit(1);
}

const lines = fs.readFileSync(roadmapPath, 'utf8').split('\n');
const changes = [];
const updated = lines.map((line, i) => {
  const m = line.match(TASK_LINE_RE);
  if (!m) return line;

  const filePath = m[4];
  const currentBox = m[2];
  const newBox = computeCheckbox(filePath);

  if (currentBox !== newBox) {
    changes.push({
      line: i + 1,
      file: filePath,
      was: currentBox === ' ' ? '[ ]' : `[${currentBox}]`,
      now: newBox === ' ' ? '[ ]' : `[${newBox}]`,
    });
    return line.replace(TASK_LINE_RE, `$1${newBox}$3$4$5`);
  }
  return line;
});

// --- Output ---
if (changes.length === 0) {
  console.log('Roadmap is already up to date.');
  process.exit(0);
}

if (!dryRun) {
  fs.writeFileSync(roadmapPath, updated.join('\n'), 'utf8');
}

const tag = dryRun ? ' [DRY RUN]' : '';
console.log(`\nRoadmap sync complete${tag} — ${changes.length} change(s):\n`);
console.log('File'.padEnd(60) + 'Was   Now');
console.log('-'.repeat(72));
changes.forEach(({ file, was, now }) => {
  console.log(file.padEnd(60) + was.padEnd(6) + now);
});
console.log('');
