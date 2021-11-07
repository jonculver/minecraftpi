import utils
import time

from mcpi_utils.firework import Firework
from mcpi import minecraft, block
from minecraftstuff import MinecraftDrawing

time.sleep(1)

# Create a minecraft instance
mc = minecraft.Minecraft.create()
mcdraw = MinecraftDrawing(mc)

# Find our current position
x, y, z = mc.player.getPos()


# Set the start position a short distance away

y = mc.getHeight(x, z)

mc.setBlocks(x-50, y, z-50, x+50, y+50, z+50, 0)
mc.setBlocks(x-50, y, z-50, x+50, y, z+50, block.IRON_BLOCK.id)

def draw_wall(x,y,z,radius, height):
    for n in range(height):
        mcdraw.drawHorizontalCircle(x, y+1+n, z, radius, block.SANDSTONE.id)

for n in range(12):
    draw_wall(x, y, z, 25-n, 12-n)

