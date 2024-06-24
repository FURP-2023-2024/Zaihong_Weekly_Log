#!/bin/bash

# Define the tag to search for
TAG="#1-projects/FURP"

# Define the source and destination directories
SOURCE_DIR="/mnt/c/Users/jacky/Obsidian Notes/"
DEST_DIR="/mnt/c/Users/jacky/FURP_LOG/Notes/"

# Find and copy files with the specified tag, overwriting if the file already exists
find "$SOURCE_DIR" -type f -exec grep -l "$TAG" {} \; | while read file; do
	filename=$(basename "$file") # Get the filename from the path
	copy_path="$DEST_DIR/$filename"
	echo "Copying $file to $copy_path"
	cp -f "$file" "$copy_path"
done

echo "File copying completed."
