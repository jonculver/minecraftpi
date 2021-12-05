import utils
from mcpi.minecraft import Minecraft
from mcpi import block
from minecraftstuff import MinecraftTurtle
from mcpi_utils.wool import WoolColors

mc = Minecraft.create()

# Find our current position
x, y, z = mc.player.getPos()

# Start a little way away and above the ground
x += 10
y += 1

# create minecraft turtle
steve = MinecraftTurtle(mc)

steve.setposition(x, y, z)
steve.speed(10)

# Draw trunk
steve.penblock(block.WOOD.id)
steve.up(90)
steve.forward(2)

# Draw Leaves
steve.penblock(block.LEAVES.id)
steve.down(90)
steve.right(90)
for i in range(7):
    width = 7-i
    steve.forward(width)
    steve.right(180)
    steve.forward(2*width)
    steve.right(180)
    steve.forward(width)
    steve.up(90)
    steve.forward(1)
    steve.down(90)

# Add baubles
mc.setBlock(x+1, y+3, z-4, block.WOOL.id, WoolColors.RED)
mc.setBlock(x+1, y+5, z+3, block.WOOL.id, WoolColors.BLUE)
mc.setBlock(x+1, y+6, z-2, block.WOOL.id, WoolColors.ORANGE)
mc.setBlock(x+1, y+7, z+1, block.WOOL.id, WoolColors.CYAN)
mc.setBlock(x+1, y+4, z-1, block.WOOL.id, WoolColors.YELLOW)
mc.setBlock(x+1, y+1, z+5, block.WOOL.id, WoolColors.RED)
mc.setBlock(x+1, y+2, z+3, block.WOOL.id, WoolColors.BLUE)
mc.setBlock(x+1, y+2, z-4, block.WOOL.id, WoolColors.ORANGE)
mc.setBlock(x+1, y+3, z+2, block.WOOL.id, WoolColors.CYAN)
mc.setBlock(x+1, y+1, z-6, block.WOOL.id, WoolColors.YELLOW)
