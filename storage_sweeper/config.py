#! python3

# config.py: Storage_Sweeper configuration file 

# Required Modules
import sys
import platform

if platform.system() == 'Windows':
    IGNORED_PATHS = [
        'C:\\Windows', 'C:\\Program Files', 'C:\\Program Files (x86)', 'C:\\ProgramData',
        'C:\\Users\\All Users', 'C:\\System Volume Information', 'C:\\Recovery'
    ]
else:
    IGNORED_PATHS = [
        '/bin', '/boot', '/dev', '/etc', '/lib', '/proc', '/run', '/sbin', '/sys', '/usr', '/var'
    ]

DEFAULT_THRESHOLD_MB = 100  # Default threshold
DEFAULT_SCAN_TYPE = 'both'  # file, folder, or both