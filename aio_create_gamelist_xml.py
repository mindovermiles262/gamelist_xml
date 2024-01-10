#!/usr/bin/env python3

import os
import re
import shutil

from dicttoxml import dicttoxml

# The directory that holds all your roms and images
INPUT_ROMS_PATH   = "/home/dipsea/data/games/nes/R-Z"
INPUT_IMAGES_PATH = "/home/dipsea/Games/thumbnails/nes/Named_Boxarts/"

# The folder where you want your images for each rom to go into
OUTPUT_IMAGES_PATH = "/home/dipsea/data/games/nes/gamelist/images"
OUTPUT_ROMS_PATH   = "/home/dipsea/data/games/nes/gamelist"

# The type of images in the images_path directory
IMAGES_EXT = ".png"

gamelist = []


def clean_filename(name, ext=None):
    """Removes parenthesis from filename"""
    regex_search = "(.*?)\("
    reg = re.split(regex_search, name)
    if len(reg) >= 3:
        filename = reg[1].strip()
        file_ext = reg[-1].split(".")[-1]
    else:
        split = reg[0].split(".")
        filename = split[0]
        file_ext = split[1]
    if ext is None:
        ext = file_ext
    return f"{filename}.{ext}"


def get_image_file(dirty_rom_name):
    """
    Searches the $INPUT_IMAGES_PATH for $dirty_rom_name, substituting the file 
    extension for $IMAGES_EXT. i.e. "game.gb" ==> "game.png".
    Also converts "&" to "_" as this is how libretro thumbnails are named.
    """
    img_filename = dirty_rom_name.rsplit(".", 1)[0] + IMAGES_EXT
    img_filename = img_filename.replace("&", "_")
    img_search_path = os.path.join(INPUT_IMAGES_PATH, img_filename)
    found_img_file = None 
    if os.path.exists(img_search_path):
        found_img_file = img_search_path
    return found_img_file



# for dirtyname in os.listdir(INPUT_ROMS_PATH):
for dirtyname in [
    "Wizards & Warriors III - Kuros...Visions of Power (USA).nes",
    "Wizards & Warriors III - Kuros...Visions of Power (USA) (Rev 1).nes",
    "doesnotexist.nes"
]:
    game = {}
    # Clean Names
    print(f"[*] Processing {dirtyname}")
    clean_romname = clean_filename(dirtyname)
    clean_imgname = clean_filename(dirtyname, "png")

    # Search for Image
    found_img_path = get_image_file(dirtyname)
    if found_img_path is None:
        print(f"[!] Image for {dirtyname} not found. Please manually add it.")
    else:
        game['box_art'] = f"./images/{clean_imgname}"
    

    # Copy rom to output dir
    input_rom_file  = os.path.join(INPUT_ROMS_PATH, dirtyname)
    output_rom_file = os.path.join(OUTPUT_ROMS_PATH, clean_romname)
    # print(f"Copying {input_rom_file} to {output_rom_file}")
    # shutils.copy(input_rom_file, output_rom_file)
    print("---")

    # Copy image to output dir

    # Add to gamelist
    game['dir'] = f"./{clean_romname}"
    gamelist.append(game)

print("+++")
print(gamelist)
print("+++")
xml = dicttoxml(gamelist, attr_type=False, root="gamelist")
print(xml)

