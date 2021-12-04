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

# Create Fireworks
rocket = Firework(mc, x, z, delay=0, color="R")
# Launch Fireworks
while not rocket.finished():
    rocket.move()
    time.sleep(0.1)

def display():
    # Create Fireworks
    rockets = []

    for i in range(10):
        gap = i * 2
        rocket = Firework(mc, x, z + gap, delay=gap)
        rockets.append(rocket)
    # Launch Fireworks
    while len(rockets) > 0:
        for r in rockets:
            r.move()
            if r.finished():
                rockets.remove(r)
        time.sleep(0.05)

for n in range(20):
    display()
