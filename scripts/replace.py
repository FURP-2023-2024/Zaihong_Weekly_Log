import os
import re


def replace_pattern(directory):
    # Regex pattern to find [[filename]]
    pattern = re.compile(r"\[\[(.*?)\]\]")

    # Only process markdown files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            # Construct the full file path
            file_path = os.path.join(directory, filename)

            # Open and read the file
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                # Replace the pattern with the markdown link format
                new_content = pattern.sub(r"[\1](\1.md)", content)

                # If the content has changed, write it back to the file
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(new_content)
                    print(f"Updated file: {file_path}")
            except Exception as e:
                print(f"Error reading or writing to file {file_path}: {e}")


# Replace 'your_directory_path' with the path to the directory you want to search in
replace_pattern("/mnt/c/Users/jacky/FURP_LOG/")
