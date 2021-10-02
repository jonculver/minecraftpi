import utils

from mcpi_utils.wool import setWoolBlock
from mcpi import minecraft

# Create a minecraft instance
mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()


list = "ROYGUMP"

r1 = "WWWWWWWWRRWWWWWWWW"
r2 = "RRRRRRRRRRRRRRRRRR"
ENGLAND = [r1] * 5 + [r2] * 2 + [r1] * 5

FRANCE = ["UUUUUUWWWWWWRRRRRR"]*12
FRANCE = ["U" * 6 + "W" * 6 + "R" * 6] * 12

US = ["WUWUWUWUWRRRRRRRRR",
      "UWUWUWUWUWWWWWWWWW"] * 3
US += ["RRRRRRRRRRRRRRRRRR",
       "WWWWWWWWWWWWWWWWWW"] * 3

WALES = ["W"*18,
         "W" * 6 + "R" + "W" * 5 + "RRRWWW",
         "WWWWRRRWWWRRRRWRWW",
         "WWWRRRRWWRRRRWWRWW",
         "W" * 5 + "RRWRRRRRWRWWW",
         "WWRRW" + "R" * 7 + "WRRWWW",
         "LLLRL" + "R" * 9 + "LLLL",
         "LLL" + "R" * 11 + "LLLL",
         "LLLLRRRRLLRRLRRLLL",
         "L" * 6 + "RLLL" * 3,
         "L" * 5 + "RRLL" * 3 + "L",
         "L" * 18]

area = US

for dy, row in enumerate(area):
    for dx, colour in enumerate(row):
        setWoolBlock(mc, x + dx + 1, y + len(area) - dy, z, colour)
