python organizer.py <target_folder> [options]

Options:
  --dry-run     Preview changes without moving anything
  --undo        Reverse the last organize operation
```

---

### Category Rules

| Folder | Extensions |
|---|---|
| `Images/` | `.jpg .jpeg .png .gif .webp .svg .bmp` |
| `Documents/` | `.pdf .docx .doc .txt .xlsx .csv .pptx` |
| `Videos/` | `.mp4 .mov .avi .mkv .wmv` |
| `Audio/` | `.mp3 .wav .flac .aac .ogg` |
| `Archives/` | `.zip .tar .gz .rar .7z` |
| `Code/` | `.py .js .html .css .json .ts .sh` |
| `Misc/` | anything that doesn't match above |

---

### Behavior Rules

**Normal run:**
1. Scan all files in the target folder (non-recursive — top level only)
2. Skip files that are already in a category subfolder
3. For each file, determine its destination folder
4. If the destination file already exists, rename the incoming file by appending `_1`, `_2`, etc. (don't overwrite)
5. Move the file
6. Write every move to `undo_log.json` as `{"from": "...", "to": "..."}`

**Dry run:**
- Print each planned move as: `[DRY RUN] report.pdf → Documents/report.pdf`
- Print a summary at the end: `X files would be moved`
- Don't touch any files, don't write the log

**Undo:**
- Read `undo_log.json`
- Move every file back to its original location in reverse order
- Delete `undo_log.json` when done
- If a file is missing (already moved/deleted), print a warning and skip it

---

### Output Examples
```
Moving: vacation.jpg → Images/vacation.jpg
Moving: notes.txt → Documents/notes.txt
Moving: unknownfile.xyz → Misc/unknownfile.xyz

Done! 3 files organized.
```
```
[DRY RUN] vacation.jpg → Images/vacation.jpg
[DRY RUN] notes.txt → Documents/notes.txt

2 files would be moved.
```
```
Undoing: Documents/notes.txt → notes.txt
Undoing: Images/vacation.jpg → vacation.jpg

Undo complete. 2 files restored.
