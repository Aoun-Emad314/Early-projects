# Interactive Bulk File Renamer

A lightweight, interactive Command Line Interface (CLI) tool built in Python to safely rename multiple files in a specific directory. 

## ✨ Features

- **Targeted Filtering:** Specify a directory and filter by file extension (e.g., `jpg`, `txt`, `pdf`), or press Enter to target all files in the folder.
- **Interactive Prompts:** The script prompts you to rename each file individually.
- **Easy Skipping:** Just press `Enter` to skip renaming a file without making any changes.
- **Smart Extensions:** If you forget to type the file extension in your new name, the script automatically reattaches the original extension for you.
- **Collision Prevention:** Built-in safety checks prevent you from accidentally overwriting an existing file if you choose a name that is already taken.
- **History Log:** Prints a complete summary of all renamed files at the end of the session.

## 🚀 Prerequisites

- Python 3.6 or higher (uses the modern `pathlib` library).
- No external dependencies required!

## 💻 Usage

1. Clone this repository or download the script.
2. Open your terminal or command prompt.
3. Run the script:
   ```bash
   python main.py
   ```
4. Follow the interactive prompts:
   - Enter the full path of the folder you want to target.
   - Enter the file extension you want to filter by (or press Enter for all files).
   - Type a new name for each file when prompted, or press Enter to skip.

## ⚠️ Note

Always double-check your file paths before running bulk operations. While this script includes safety checks against overwriting, it's good practice to test it on a backup folder first if you are dealing with sensitive data.