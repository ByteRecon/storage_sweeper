#! python3

# scanner.py: File/folder scanner for Storage_Sweeper 

# Required Modules
import os
from .utils import is_ignored_path

# Get the size of folder or file
def get_size(path):
    total = 0
    if os.path.isfile(path):
        return os.path.getsize(path)
    for root, _, files in os.walk(path):
        for f in files:
            try:
                fp = os.path.join(root, f)
                total += os.path.getsize(fp)
            except:
                continue
    return total

# Scan files and folders against given or default threshold
def scan_directory(path, threshold_mb, scan_type):
    files = []
    folders = []
    threshold_bytes = threshold_mb * 1024 * 1024
    for root, dirs, file_list in os.walk(path):
        if is_ignored_path(root):
            continue

        if scan_type in ['folder', 'both']:
            try:
                size = get_size(root)
                if size >= threshold_bytes:
                    folders.append((root, size))
            except:
                continue

        if scan_type in ['file', 'both']:
            for file in file_list:
                file_path = os.path.join(root, file)
                if is_ignored_path(file_path):
                    continue
                try:
                    size = os.path.getsize(file_path)
                    if size >= threshold_bytes:
                        files.append((file_path, size))
                except:
                    continue
    return folders, files
