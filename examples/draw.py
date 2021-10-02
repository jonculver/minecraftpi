#
# Example code for using the pictures utility to build images
#

import utils

from mcpi_utils.pictures import build_image

from mcpi_utils.wool import setWoolBlock
from mcpi import minecraft

# Create a minecraft instance
mc = minecraft.Minecraft.create()

build_image(mc, "images/minecraft_logo.png", 64)
