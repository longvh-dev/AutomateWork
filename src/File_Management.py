# Sorting Files in a Directory
def sort_files(directory_path):
    import os
    from shutil import move
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            file_extension = filename.split('.')[-1]
            destination_directory = os.path.join(directory_path, file_extension)
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            move(os.path.join(directory_path, filename), os.path.join(destination_directory, filename))


# Removing Empty Folders
def remove_empty_folders(directory_path):
    import os
    for root, dirs, files in os.walk(directory_path, topdown = False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)


# Renaming Multiple Files
def rename_files(directory_path, old_name, new_name):
    import os
    for filename in os.listdir(directory_path):
        if old_name in filename:
            new_filename = filename.replace(old_name, new_name)
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
