# XML Gamelist

A collection of scripts to create a gamelist.xml for Emulation Station.

`create_gamelist_xml.py` ==> Create gamelist.xml contaning the path, image, and name of all the files in a specific directory

`get_images_for_files.py` ==> Given a directory of roms, search a directory of images (libretro thumbnails) for that filename's image. Then copy it to a destination directory.

`aio_create_gamelist_xml.py` ==> All In One. WIP. Given a list of rom files, search for images, copy them to a destination address, and create a gamelist.xml file for each of the entries.

`remove_parens_from_roms.py` ==> Renames romfiles, removing the parethesis. i.e. `Game (US, Japan) (Rev 2).rom` will become `Game.rom`

# Quickstart

1. Download the libretro thumbnails for your specific system
2. Update [get_images_for_files](get_images_for_files.py) with the correct data:
  * `roms_dir` --> The directory where all your game roms are stored.
  * `roms_images_dir` --> The directory where the images are copied to. `images` directory inside your roms dir, usually.
  * `images_path` --> The directory where the (libretro) images are saved. Usually ends with `Named_Boxarts`
3. Run `./get_images_for_files` -- Read the output, look for any errors and correct them.
4. Update [create_gamelist_xml](create_gamelist_xml.py) with the proper directories.
5. Run `./create_gamelist_xml.py`
6. Copy the generated `.xml` file to your roms and images directory. 
7. Copy roms directory (with images and `gamelist.xml`) onto your device
8. Profit
