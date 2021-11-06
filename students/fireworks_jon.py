import utils
import time

from mcpi_utils.firework import Firework
from mcpi import minecraft

# Create a minecraft instance
mc = minecraft.Minecraft.create()
mc.setting("time", "night")

# Find our current position
x, y, z = mc.player.getPos()

# Set the start position a short distance away
x += 10

# Create Fireworks
rockets = []

# Create a square of fireworks. Start by setting the delay, x delta and z delta
# to zero, and modify them as we move around the sides
delay = 0
dx = 0
dz = 0

# First side of a square - increase Z
for i in range(10):
    dz += 2
    delay += 2
    rocket = Firework(mc, x + dx, z + dz, delay=delay)
    rockets.append(rocket)

# Second side of a square - increase X
for i in range(10):
    dx += 2
    delay += 2
    rocket = Firework(mc, x + dx, z + dz, delay=delay)
    rockets.append(rocket)

# Third side of a square - decrease Z
for i in range(10):
    dz -= 2
    delay += 2
    rocket = Firework(mc, x + dx, z + dz, delay=delay)
    rockets.append(rocket)

# Fourth side of a square - decrease X
for i in range(10):
    dx -= 2
    delay += 2
    rocket = Firework(mc, x + dx, z + dz, delay=delay)
    rockets.append(rocket)

# Launch Fireworks
while len(rockets) > 0:
    for r in rockets:
        r.move()
        if r.finished():
            rockets.remove(r) 
    time.sleep(0.01)