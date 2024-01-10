# XML Gamelist

A collection of scripts to create a gamelist.xml for Emulation Station.

`create_gamelist_xml.py` ==> Create gamelist.xml contaning the path, image, and name of all the files in a specific directory

`get_images_for_files.py` ==> Given a directory of roms, search a directory of images (libretro thumbnails) for that filename's image. Then copy it to a destination directory.

`aio_create_gamelist_xml.py` ==> All In One. WIP. Given a list of rom files, search for images, copy them to a destination address, and create a gamelist.xml file for each of the entries.

`remove_parens_from_roms.py` ==> Renames romfiles, removing the parethesis. i.e. `Game (US, Japan) (Rev 2).rom` will become `Game.rom`
