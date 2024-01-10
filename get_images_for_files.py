#!/usr/bin/env python3

#
# This script will iterate over all the files in the `roms_dir` directory, and
# search the `images_path` directory to find a matching .png image file. If
# found, it will copy the image file to the `roms_images_dir` path.
#

import os
import shutil

# The directory that holds all your roms
roms_dir = "snes/T-Z"

# The folder where you want your images for each rom to go into
roms_images_dir = "/home/dipsea/snes"

# The location of all the thumbnail images in PNG format
images_path = "/home/dipsea/Games/thumbnails/snes/Named_Boxarts/"

# The type of images in the images_path directory
images_ext = ".png"

for romfile in os.listdir(roms_dir):
    # yoshi & friends.gb ==> yoshi _ friends.png
    img_filename = romfile.rsplit(".", 1)[0] + images_ext # game.gb ==> game.png
    img_filename = img_filename.replace("&", "_")

    img_path= os.path.join(images_path, img_filename)
    if os.path.exists(img_path):
        rom_image_path = os.path.join(roms_images_dir, img_filename)
        shutil.copyfile(img_path, rom_image_path) 
    else:
        print(f"[!] Not Found {img_filename}")


