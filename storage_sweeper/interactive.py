#! python3

# interactive.py: Storage_Sweeper review and select screen

# Required Modules
from .utils import format_size

ascii_banner = r"""


 .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. 
/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \
\ \/\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ \/ /
 \/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\/ / 
 / /\      ___             _               ___                                           / /\ 
/ /\ \    F _ ",  _    _  FJ_     ____    F _ ",    ____     ____     ____    _ ___     / /\ \
\ \/ /   J `-'(| J |  | LJ  _|   F __ J  J `-'(|   F __ J   F ___J.  F __ J  J '__ J    \ \/ /
 \/ /    | ,--.\ | |  | || |-'  | _____J |  _  L  | _____J | |---LJ | |--| | | |__| |    \/ / 
 / /\    F L__J \F L__J JF |__-.F L___--.F |_\  L F L___--.F L___--.F L__J J F L  J J    / /\ 
/ /\ \  J_______J)-____  \_____J\______/J__| \\__J\______/J\______/J\______/J__L  J__L  / /\ \
\ \/ /  |_______J\______/J_____FJ______F|__|  J__|J______F J______F J______F|__L  J__|  \ \/ /
 \/ /            J______F                                                                \/ / 
 / /\.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--./ /\ 
/ /\ \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \/\ \
\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--' 
            
            https://github.com/ByteRecon



 _____ _                               _____                                   
/  ___| |                             /  ___|                                  
\ `--.| |_ ___  _ __ __ _  __ _  ___  \ `--.__      _____  ___ _ __   ___ _ __ 
 `--. | __/ _ \| '__/ _` |/ _` |/ _ \  `--. \ \ /\ / / _ \/ _ | '_ \ / _ | '__|
/\__/ | || (_) | | | (_| | (_| |  __/ /\__/ /\ V  V |  __|  __| |_) |  __| |   
\____/ \__\___/|_|  \__,_|\__, |\___| \____/  \_/\_/ \___|\___| .__/ \___|_|   
                           __/ |                              | |              
                          |___/                               |_|              


"""

# Function for review and select screen
def review_and_select(folders, files):
    while True:
        if not folders and not files:
            print(ascii_banner)
            print("No items found matching criteria.")
            return []

        # List files and folders above given or default threshold
        print(ascii_banner)
        print("\nFolders found:")
        for idx, (path, size) in enumerate(folders):
            print(f"[F{idx+1}] {path} ({format_size(size)})")

        offset = len(folders)
        print("\nFiles found:")
        for idx, (path, size) in enumerate(files):
            print(f"[L{idx+1}] {path} ({format_size(size)})")

        selected = input("\nSelect items by number (e.g. F1,F2,L4), 'a' for all, 'e' to exit: ").strip()
        if selected.lower() == 'e':
            return []
        elif selected.lower() == 'a':
            return [path for path, _ in folders + files]
        else:
            try:
                indices = selected.split(',')
                selected_paths = []
                for i in indices:
                    i = i.strip().upper()
                    if i.startswith('F'):
                        index = int(i[1:]) - 1
                        if 0 <= index < len(folders):
                            selected_paths.append(folders[index][0])
                    elif i.startswith('L'):
                        index = int(i[1:]) - 1
                        if 0 <= index < len(files):
                            selected_paths.append(files[index][0])
                return selected_paths
            except:
                print("Invalid input. Try again.")