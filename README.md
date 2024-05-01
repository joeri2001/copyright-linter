## Copyright Updater

This Python script automates the process of updating or adding copyright notices within your code files.  It's designed to ensure your copyright information stays current.

**Key Features**

* **Customizable:** Supports multiple file extensions and their corresponding comment prefixes.
* **Intelligent:** Updates existing copyright notices or adds a new notice as needed.
* **Error Handling:** Handles files with potential encoding issues.

**How it Works**

1. Scans a specified directory for supported file types.
2. Reads the contents of each file.
3. Searches for an existing copyright notice matching the defined pattern.
    * If found, updates the year to the current year.
    * If not found, inserts a new copyright notice at the beginning of the file.
4. Detects and gracefully handles files with encoding errors.

**Usage**

1. **Configure `file_extensions`:**  Modify the `file_extensions` dictionary to include the file extensions you want to target and their corresponding comment prefixes (e.g., '//' or '#').

2. **Run the Script:**
   `python copyright.py`


### Example file_extensions

```
file_extensions = {
    ".html": ("<!--", "-->")
    ".css": "//",
    ".ts": "//",
    ".yml": "#"
}