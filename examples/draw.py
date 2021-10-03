#
# Example code for using the pictures utility to build images
#
import utils

from mcpi_utils.pictures import build_image

from mcpi_utils.wool import setWoolBlock
from mcpi import minecraft

# Create a minecraft instance
mc = minecraft.Minecraft.create()

# Find the player location and set the start location 
# to be a short distance away
x, y, z = mc.player.getPos()
z -= 10

# Draw the image at these cooordinates, with size 48 blocks
build_image(mc, x, y, z, "images/raspberrypi.png", 48)
