# New Device Setup

After cloning this repository, several folders need to be created because they are gitignored.

## Step 1: Set Up context_knowledge/

```bash
mkdir -p context_knowledge
# Then run /init-context in Claude Code to populate files
```

## Step 2: Set Up features/ (OneDrive Symlink)

```bash
# Create OneDrive folder (first time only)
mkdir -p ~/Library/CloudStorage/OneDrive-Personal/Claude_Balance_Features

# Create symlink from repo root
ln -s ~/Library/CloudStorage/OneDrive-Personal/Claude_Balance_Features features
```

## Step 3: Set Up Transcriptions/ (Google Drive Symlinks)

```bash
mkdir -p Transcriptions

# Link to user interview transcripts (adjust email for your account)
ln -s ~/Library/CloudStorage/GoogleDrive-<your-email>/Mi\ unidad/Meet\ Recordings/Trans_MD Transcriptions/transcription_source

# Link to first consultation transcripts
ln -s ~/Library/CloudStorage/GoogleDrive-<your-email>/Mi\ unidad/Meet\ Recordings/1st_DoctorTranscript Transcriptions/1st_consultation_source
```

## Step 4: Set Up User_discovery/.env

```bash
echo 'OPENAI_API_KEY=your-key-here' > User_discovery/.env
```

## Step 5: Verify Setup

```bash
ls context_knowledge/     # Should have files after /init-context
ls features/              # Should show OneDrive contents
ls Transcriptions/        # Should show symlinks
```
