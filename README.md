# File Organizer

A command-line tool that automatically sorts files in a folder into categorized subfolders, with dry-run preview and undo support.

---

## Files

| File | Description |
|---|---|
| `organizer.py` | Main script — scans, moves, and restores files |
| `populate_test.sh` | Bash script to generate test files and folders |

---

## Usage

```bash
python organizer.py <folder> [options]
```

| Command | Description |
|---|---|
| `python organizer.py /path/to/folder` | Organize files into subfolders |
| `python organizer.py /path/to/folder --dry-run` | Preview what would be moved without doing anything |
| `python organizer.py /path/to/folder --undo` | Reverse the last organize operation |

---

## Categories

Files are sorted into the following subfolders based on extension:

| Folder | Extensions |
|---|---|
| `Images/` | `.jpg .jpeg .png .gif .webp .svg .bmp` |
| `Documents/` | `.pdf .docx .doc .txt .xlsx .csv .pptx` |
| `Videos/` | `.mp4 .mov .avi .mkv .wmv` |
| `Audio/` | `.mp3 .wav .flac .aac .ogg` |
| `Archives/` | `.zip .tar .gz .rar .7z` |
| `Code/` | `.py .js .html .css .json .ts .sh` |
| `Misc/` | Anything that doesn't match the above |

---

## Behavior

- **Top-level only** — subfolders inside the target folder are not touched
- **Duplicate handling** — if a file with the same name already exists in the destination, it is renamed with a numeric suffix (e.g. `photo_1.jpg`, `photo_2.jpg`)
- **Undo log** — every move is recorded to `undo_log.json` in the working directory; `--undo` reads this file and reverses all moves in reverse order, then deletes the log
- **Missing files on undo** — if a file can't be found at its expected location, a warning is printed and it is skipped

---

## Testing

Use the included bash script to populate a folder with sample files:

```bash
# First time only
chmod +x populate_test.sh

# Create test files in ./test_folder (default)
./populate_test.sh

# Or specify a custom path
./populate_test.sh /path/to/folder
```

This creates dummy files across all supported categories, plus a subfolder with a nested file to verify that subfolders are correctly skipped by the organizer.

### Recommended test workflow

```bash
# 1. Populate
./populate_test.sh

# 2. Preview
python organizer.py ./test_folder --dry-run

# 3. Organize
python organizer.py ./test_folder

# 4. Undo
python organizer.py ./test_folder --undo
```

---

## Requirements

- Python 3.x
- Standard library only (`os`, `shutil`, `json`, `argparse`) — no installs needed
