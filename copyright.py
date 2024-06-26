import os
import datetime
import re

current_year = datetime.datetime.now().year
copyright_string = "Copyright (c) YourCompany."
copyright_end = ""

file_extensions = {
    ".py": "#",
}

def update_copyright(content, comment_prefix, comment_end):
    lines = content.splitlines()  
    modified = False
    pattern = r"{}".format(re.escape(comment_prefix + " " + copyright_string)) 

    for i in range(len(lines)):
        match = re.search(pattern, lines[i])
        if match:
            lines[i] = re.sub(r"\d{4}.*" + re.escape(comment_end), str(current_year) + comment_end, lines[i])
            modified = True
            break 

    if not modified:
        if lines:  
            if not lines[0].strip():
                lines.insert(0, f"{comment_prefix} {copyright_string} {current_year} {comment_end}")
            else:
                lines.insert(0, f"{comment_prefix} {copyright_string} {current_year} {comment_end}\n")  
        else:
            lines.append(f"{comment_prefix} {copyright_string} {current_year} {comment_end}\n") 

    if lines:
        if not lines[0].endswith('\n'):  
            lines[0] += '\n'  
        if len(lines) > 1 and not lines[1].strip():
            del lines[1] 

    result = '\n'.join(lines)
    if content.endswith('\n'):  
        result += '\n'
    return result, modified

for root, dirs, files in os.walk(os.path.dirname(__file__)):
    for file in files:
        for extension, comment_info in file_extensions.items():
            if file.endswith(extension):
                path = os.path.join(root, file)
                print(f"Processing: {path}")  
                with open(path, 'r+', encoding='utf-8', errors='ignore') as f:
                    try:
                        content = f.read()
                    except UnicodeDecodeError:
                        print(f"Unable to decode file: {path}")
                        continue
                    f.seek(0)
                    f.truncate()
                    if isinstance(comment_info, tuple):
                        new_content, modified = update_copyright(content, *comment_info) 
                    else:
                        new_content, modified = update_copyright(content, comment_info, "")
                    f.write(new_content)

                    if modified:
                        print(f"Updated: {path}") 
