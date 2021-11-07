import utils
import time

from mcpi_utils.firework import Firework
from mcpi import minecraft

time.sleep(5)

# Create a minecraft instance
mc = minecraft.Minecraft.create()

# Find our current position
x, y, z = mc.player.getPos()

# Set the start position a short distance away
x += 10
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
    