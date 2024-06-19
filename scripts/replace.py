import os
import re
import urllib.parse


def url_encode_spaces(filename):
    # Encode spaces in the filename for URL usage
    return urllib.parse.quote(filename)


def replace_pattern(directory):
    # Regex pattern to find [[filename]]
    pattern = re.compile(r"\[\[(.*?)\]\]")

    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)

            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                def replace(match):
                    match_group = match.group(1)  # Get the captured group \1
                    return f"[{match_group}]({url_encode_spaces(match_group)}.md)"

                new_content = pattern.sub(replace, content)

                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(new_content)
                    print(f"Updated file: {file_path}")
            except Exception as e:
                print(f"Error reading or writing to file {file_path}: {e}")


# Replace 'your_directory_path' with the path to the directory you want to search in
replace_pattern("/mnt/c/Users/jacky/FURP_LOG/")
