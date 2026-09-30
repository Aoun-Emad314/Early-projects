from pathlib import Path


def main():
    # Target a directory: Tell the program exactly which folder to look inside.
    file_location, file_type = target_dir()

    # Read the contents: Ask the operating system for a list of everything inside that folder.

    # Filter the list: Ignore folders and files you don't want to touch (like keeping only .jpg files).
    filtered_files = read_filter(file_location, file_type)
    # Construct the new name: Take the old filename and attach your new prefix, suffix, or timestamp to it.

    # Execute the rename: Tell the operating system to replace the old path with the new path.
    rename_files(filtered_files)


def target_dir():
    print("✨ Targeting directory:STARTED!")
    path = Path(input("Enter the file location path :"))
    if not path.exists() or not path.is_dir():
        print("Error code 404: That directory does not exist!")
        exit()
    f_type = (
        (input("Type of file you wanna rename(pdf,txt,jpg,etc...):"))
        .strip()
        .lstrip(".")
    )

    print(f"Your current working dir is {Path.cwd()}")
    return path, f_type


def read_filter(path, f_type):
    print("✨ Reading & Filtering:STARTED!")
    filtered_files_path = []
    if f_type == "":
        for i in path.iterdir():
            if i.is_file():
                print(i.name)
                filtered_files_path.append(i)

    else:
        for i in path.glob(f"*.{f_type}"):
            print(i.name)
            filtered_files_path.append(i)
    return filtered_files_path


def rename_files(fnames):
    print("✨ File renaming:STARTED!")
    logs = []
    for fname in fnames:
        new_name = input(
            f"What do you want to rename this file ({fname.name}),press enter to skip!:\n"
        )
        if new_name == "":
            continue
        if not new_name.endswith(fname.suffix):
            new_name = new_name + fname.suffix
        new_path = fname.with_name(f"{new_name}")
        if new_path.exists():
            print("Error: The file name is already exists!,The file skipped!")
            continue
        fname.rename(new_path)
        log = f"Renamed: {fname.name} -> {new_name}"
        print(log)
        logs.append(log)
    print("=" * 40)
    print("HISTORY:")
    for i in logs:
        print(i)
    print("=" * 40)


if __name__ == "__main__":

    main()
