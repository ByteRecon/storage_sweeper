#! python3

# main.py: Storage_Sweeper is a python application that sweeps your pc for files and folders that are larger
#             than a given threshold, displays those files, and allows you to remove, move, or copy them to another location

# Required Modules
import argparse
import os
from .scanner import scan_directory
from .interactive import review_and_select
from .actions import delete_items, move_items, copy_items
from .config import DEFAULT_THRESHOLD_MB, DEFAULT_SCAN_TYPE

def main():
    parser = argparse.ArgumentParser(description="Storage Sweeper - Clean up large files/folders")
    parser.add_argument('--path', type=str, default=os.path.expanduser('~'), help='Path to scan')
    parser.add_argument('--threshold', type=int, default=DEFAULT_THRESHOLD_MB, help='Size threshold in MB')
    parser.add_argument('--type', type=str, choices=['file', 'folder', 'both'], default=DEFAULT_SCAN_TYPE)
    args = parser.parse_args()

    while True:
        print("\n🔍 Scanning...")
        folders, files = scan_directory(args.path, args.threshold, args.type)

        selected_paths = review_and_select(folders, files)
        if not selected_paths:
            print("No files selected. Exiting.")
            break

        print("\nWhat would you like to do with the selected files?")
        print("1. Delete\n2. Move\n3. Copy\n4. Back to selection\n5. Exit")
        action = input("Enter option (1/2/3/4/5): ").strip()

        if action == '1':
            delete_items(selected_paths)
        elif action == '2':
            target = input("Enter target directory for move: ").strip()
            move_items(selected_paths, target)
        elif action == '3':
            target = input("Enter target directory for copy: ").strip()
            copy_items(selected_paths, target)
        elif action == '4':
            continue
        elif action == '5':
            print("Exiting.")
            break
        else:
            print("Invalid option. Returning to selection.")

if __name__ == '__main__':
    main()
