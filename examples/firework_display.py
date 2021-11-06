from mcpi import minecraft
import time
from random import randint

import utils
from mcpi_utils.firework import Firework


# Create a minecraft instance
mc = minecraft.Minecraft.create()

# Get the player location as the center point for the display
x, y, z = mc.player.getPos()

# A list of active fireworks
fireworks = []

TIME = 100

for i in range(TIME):
    # Every few ticks launch another rocket. Leave time at the end for everything to finish
    if i % 4 == 0 and i < TIME - 30:
        # Create a new rocket in a random position near the player and add it to the list
        fireworks.append(Firework(mc, x + randint(-20, 20), z + randint(-20, 20)))
    
    # Advance every rocket in the list one space. Once done remove them from the list
    for fw in fireworks:
        if fw.finished():
            fireworks.remove(fw)
        else:
            fw.move()

    # Wait a short time to make a suitable frame rate
    time.sleep(0.05)
