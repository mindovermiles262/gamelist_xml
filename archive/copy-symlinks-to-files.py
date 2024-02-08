#!/usr/bin/env python3

import os
import shutil

walk_dir = "."

for filename in os.listdir(walk_dir):
    file = os.path.join(walk_dir, filename)
    try:
        if os.path.islink(file):
            target = os.readlink(file)
            print(f"Target File is {target}")
            os.unlink(file)
            print(f"Unlinked {file}")
            shutil.copyfile(target, file)
    except:
        print(f"[!] ERROR with {file}")
