import utils
from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi_utils.wool import setWoolBlock

mc = Minecraft.create()

# Find our current position
x, y, z = mc.player.getPos()

# Start a little way away
x += 10



# Draw Leaves
for i in range(7):
    width = 7-i
    mc.setBlocks(x, y+2+i, z-width,
                 x, y+2+i, z+width,
                 block.LEAVES.id)

# Add baubles
setWoolBlock(mc, x, y+3, z-4, "R")
setWoolBlock(mc, x, y+5, z+3, "B")
setWoolBlock(mc, x, y+6, z-2, "O")
setWoolBlock(mc, x, y+7, z+1, "C")
setWoolBlock(mc, x, y+4, z-1, "Y")
setWoolBlock(mc, x, y+2, z+3, "B")
setWoolBlock(mc, x, y+2, z-4, "O")
setWoolBlock(mc, x, y+3, z+2, "C")

# Add the star
mc.setBlock(x, y+9, z, block.GLOWSTONE_BLOCK.id)
