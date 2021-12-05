# Christmas.py - While running, hitting blocks of various different types will
#                draw Christmas images and cover the ground with snow

import utils
import time
from mcpi_utils.pictures import build_image

from mcpi import minecraft, block

mc = minecraft.Minecraft.create()

mc.postToChat("Merry Christmas")

# Dictionary of block types to images
block_map = {
    block.COAL_ORE.id: "tree",
    block.IRON_ORE.id: "penguin",
    block.GOLD_ORE.id: "santa",
    block.DIAMOND_ORE.id: "snowman",
    block.LAPIS_LAZULI_ORE.id: "polarbear",
    block.REDSTONE_ORE.id: "sleigh"
}

def snow(mc, x, z):
    """
    Cover the area around the given x,z coordinate with snow
    """
    for dx in range(x - 10, x + 10):
        for dz in range(z - 10, z + 10):
            mc.setBlock(dx, mc.getHeight(dx, dz), dz, block.SNOW)


def create_image_at(mc, x, y, z):
    """
    Draw an picture at a given (x,z) coordinate. The picture
    chosen depends on the given block type 
    """
    b = mc.getBlock(x, y, z)
    if b == block.SNOW_BLOCK.id:
        mc.postToChat("Snowing")
        snow(mc, x, z)
    elif b in block_map:
        image = block_map[b]
        mc.postToChat("Drawing {}".format(image))
        build_image(mc, x, y, z, 
                    "images/christmas/" + image + ".png",
                    40)

while True:
    time.sleep(0.1)
    events = mc.events.pollBlockHits()

    if len(events) > 0:
        # Something has been hit. Look at the last element
        event = events[-1]
        create_image_at(mc, event.pos.x, event.pos.y, event.pos.z)
