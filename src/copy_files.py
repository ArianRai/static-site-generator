import os
import shutil


def copy_files(source_dir_path, dest_dir_path):
    if os.path.exists(dest_dir_path):
        shutil.rmtree(dest_dir_path)
    os.mkdir(dest_dir_path)
    files = os.listdir(source_dir_path)
    for file in files:
        from_path = os.path.join(source_dir_path, file)
        dest_path = os.path.join(dest_dir_path, file)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files(from_path, dest_path)
