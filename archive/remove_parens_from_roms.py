#!/usr/bin/env python3

import os
import re
import shutil

# rom_dir="A-F"
# rom_dir="G-Q"
rom_dir="/home/dipsea/data/games/gb/R-Z"
clean_dir="clean"

regex_search="(.*?)\("

# for filename in os.listdir(rom_dir):
#   file = os.path.join(rom_dir, filename)
#   if os.path.isfile(file):
#     new_title = re.split(regex_search, filename)[1].strip()
#     new_file = os.path.join(clean_dir, new_title)
#     new_file = new_file + ".nes"
#     print(new_file)
#     shutil.copy(file, new_file)


def clean_filename(filename: str, path: str):
  file = os.path.join(path, filename)
  if os.path.isfile(file):
    new_title = re.split(regex_search, filename)[1].strip()
    new_file = os.path.join(clean_dir, new_title)
    # print(new_file)
    # shutil.copy(file, new_file)
    return new_file


for filename in os.listdir(rom_dir):
  clean_filename(filename=filename, path=rom_dir)