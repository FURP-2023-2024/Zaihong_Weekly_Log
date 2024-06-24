import os
import re
import urllib.parse

# Store the repository name
REPO_NAME = "FURP-2023-2024/Zaihong_Weekly_Log"


def url_encode_spaces(filename):
    # Encode spaces in the filename for URL usage
    return urllib.parse.quote(filename)


def create_github_link(filename):
    # Create an absolute link to the raw file on GitHub
    base_url = f"https://github.com/{REPO_NAME}"
    return f"[{filename}]({base_url}/blob/main/Notes/{url_encode_spaces(filename)}.md)"


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
                    return create_github_link(match_group)

                new_content = pattern.sub(replace, content)

                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(new_content)
                    print(f"Updated file: {file_path}")
            except Exception as e:
                print(f"Error reading or writing to file {file_path}: {e}")


# Replace 'your_directory_path' with the path to the directory you want to search in
replace_pattern("/mnt/c/Users/jacky/FURP_LOG/Notes/")
