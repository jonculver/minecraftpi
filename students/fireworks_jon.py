import utils

from mcpi_utils.firework import Firework
from mcpi import minecraft

# Create a minecraft instance
mc = minecraft.Minecraft.create()

# Find our current position
x, y, z = mc.player.getPos()

# Set the start position a short distance away
x += 10

fw = Firework(mc, x, z)
