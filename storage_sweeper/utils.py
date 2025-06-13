#! python3

# utils.py: Storage_Sweeper helper functions

# Required Modules
import os
from .config import IGNORED_PATHS

def format_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def is_ignored_path(path):
    return any(path.startswith(ignored) for ignored in IGNORED_PATHS) or '/.' in path
