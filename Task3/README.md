# File Organizer

This is a Python script that automates the process of organizing files within a folder by sorting them into subfolders based on their file types. It helps manage cluttered directories, such as a `Downloads` folder, by categorizing files into subfolders like `Images`, `Documents`, `Videos`, etc.

## Features

- **Automatic Subfolder Creation**: Creates subfolders for predefined categories like Images, Documents, Videos, Music, Archives, and Others.
- **File Categorization**: Moves files into appropriate subfolders based on their extensions.
- **Handles Unrecognized Files**: Files that do not match any predefined category are placed in an `Others` folder.
- **Non-Recursive**: Does not process subdirectories to avoid interference with existing folder structures.

## File Categories

| Category   | Extensions                                      |
|------------|------------------------------------------------|
| Images     | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff` |
| Documents  | `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.txt` |
| Videos     | `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`          |
| Music      | `.mp3`, `.wav`, `.aac`, `.flac`                |
| Archives   | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`           |
| Others     | All other unrecognized file types              |


## Usage

1. Open a terminal or command prompt.
2. Run the script using the following command:
   ```bash
   python file_organizer.py
   ```
3. Enter the path to the folder you want to organize when prompted. For example:
   ```
   Enter the folder path to organize: /path/to/your/folder
   ```
4. The script will create subfolders within the specified folder and move files accordingly.


## Dependencies

- Python 3.6+
- `os` and `shutil` (part of Python's standard library)

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve the script.


