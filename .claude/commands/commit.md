Analyze all changes (git status, git diff --stat, git diff), review recent commits for style (git log --oneline -5), then stage specific files and commit with a descriptive message. Format: imperative headline under 70 chars + bullet-point body explaining what was done. Use a HEREDOC for the message. Skip .obsidian/ and IDE state files. Never push, never use git add -A, never amend unless asked. End with Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

## Changelog Integration

After analyzing the diff, check if any staged files match these paths:
- `.claude/skills/` (any file)
- `.claude/commands/`
- `CLAUDE.md`
- `copier.yml`

If any match, this is a **system commit**. Before staging:

1. Ask the user: "System files are changing. One-line reason for the changelog?"
2. Infer the change type from the diff:
   - **Added** — new files, new skills, new commands
   - **Changed** — modifications to existing skills, commands, or CLAUDE.md
   - **Fixed** — bug fixes, broken behavior corrected
   - **Removed** — deleted files or skills
3. Append one or more bullet points under the appropriate subsection(s) inside `## [Unreleased]` in `CHANGELOG.md`. Format:

```
- `path/to/file` — one-line description of what changed and why
```

   If the `## [Unreleased]` section has no content yet, add the subsection header(s) before the bullets:

```
### Added
- ...

### Changed
- ...
```

   Only include subsections that have entries. Never add empty subsection headers.

4. Stage `CHANGELOG.md` as part of the commit.
5. Include the reason in the commit message body alongside the other bullet points.

## Skill Version Bump

After the changelog step, check if any staged files are inside `.claude/skills/SKILLNAME/` for one or more skills.

For each affected skill:
1. Read the current `version` field from `.claude/skills/SKILLNAME/SKILL.md`
2. Ask: "Bump version for [skill]? Current: X.Y — enter new version or press Enter to skip"
3. If the user provides a new version:
   - Update the `version:` field in `SKILL.md`
   - Stage the updated `SKILL.md`
   - Add the version bump to the changelog entry and commit message

If no skill files are staged, skip this step entirely.
