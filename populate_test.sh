#!/bin/bash

TARGET=${1:-./test_folder}

mkdir -p "$TARGET"
mkdir -p "$TARGET/subfolder"

# Images
touch "$TARGET/vacation.jpg"
touch "$TARGET/screenshot.png"
touch "$TARGET/logo.svg"

# Documents
touch "$TARGET/report.pdf"
touch "$TARGET/notes.txt"
touch "$TARGET/budget.xlsx"

# Videos
touch "$TARGET/clip.mp4"
touch "$TARGET/recording.mov"

# Audio
touch "$TARGET/song.mp3"
touch "$TARGET/podcast.flac"

# Archives
touch "$TARGET/backup.zip"
touch "$TARGET/archive.tar"

# Code
touch "$TARGET/script.py"
touch "$TARGET/index.html"

# Misc
touch "$TARGET/mystery.xyz"
touch "$TARGET/unknownfile.abc"

# Subfolder (should be skipped by organizer)
touch "$TARGET/subfolder/nested_file.mp3"

echo "Test files created in $TARGET"
