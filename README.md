# Storage Sweeper CLI

```
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
```

A simple CLI tool to find large files or folders and interactively delete, move, or copy them.

## Usage

```bash
python main.py --path /home/user --threshold 500 --type both
or
python -m storage_sweeper --path /home/user --threshold 500 --type both
```

- `--path`: Directory to scan (default: home dir)
- `--threshold`: Minimum size in MB (default: 100)
- `--type`: `file`, `folder`, or `both`

Then select files and choose an action interactively.

---

Safe by default: system folders and hidden files are ignored unless manually overridden.

Cross-platform: uses OS-specific ignored directories on Linux/macOS and Windows.