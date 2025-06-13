#! python3

# actions.py: Post scan options for Storage_Sweeper 

# Required Modules
import os
import shutil

def delete_items(paths):
    for path in paths:
        confirm = input(f"Delete {path}? (y/n): ").strip().lower()
        if confirm == 'y':
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                print(f"Deleted {path}")
            except Exception as e:
                print(f"Failed to delete {path}: {e}")

def move_items(paths, target_dir):
    for path in paths:
        try:
            shutil.move(path, target_dir)
            print(f"Moved {path} to {target_dir}")
        except Exception as e:
            print(f"Failed to move {path}: {e}")

def copy_items(paths, target_dir):
    for path in paths:
        try:
            dest = os.path.join(target_dir, os.path.basename(path))
            if os.path.isdir(path):
                shutil.copytree(path, dest)
            else:
                shutil.copy2(path, dest)
            print(f"Copied {path} to {dest}")
        except Exception as e:
            print(f"Failed to copy {path}: {e}")