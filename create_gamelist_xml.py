#!/usr/bin/env python3

#
# Given a directory containing a bunch of rom files, create a gamelist.xml file
# with the following format for each game:
# <gameList>
#   <game>
#     <path>./Yogi Bear - Great Balloon Blast (USA).gbc</path>
#     <name>Yogi Bear - Great Balloon Blast</name>
#     <playcount>0</playcount>
#     <image>./images/Yogi Bear - Great Balloon Blast (USA).png</image>
#   </game>
#   <game>
#     < ... >
#   </game>
# </gameList>
#
# `get_images_for_files.py`` can be used to create the directory structure for
# this script
#

import os
import re
from dicttoxml import dicttoxml

ROMS_DIR="/home/dipsea/data/games/segacd"
OUTFILE="segacd.xml"

# The name of the folder inside of ROMS_DIR where images are stored
IMAGES_DIR="images"

gamelist = []

def clean_filename(filename: str):
    regex_search="(.*?)\("
    new_title = re.split(regex_search, filename)[1].strip()
    return new_title

for romfile in os.listdir(ROMS_DIR):
    # Do not process if the Images Directory
    if romfile in [IMAGES_DIR, "gamelist.xml"]:
        continue
    game_dict = {}
    filename = romfile.rsplit(".", 1)[0]
    game_dict['path'] = f"./{romfile}"
    game_dict['name'] = clean_filename(filename)
    game_dict['playcount'] = 0
    # Image files sub & for _
    game_dict['image'] = f"./{IMAGES_DIR}/{filename}.png".replace("&", "_")
    gamelist.append(game_dict)

xml = dicttoxml(
    gamelist,
    item_func=lambda x: 'game',
    custom_root="gameList",
    attr_type=False
).decode()

with open(OUTFILE, "w") as f:
    f.write(str(xml))
    f.close()