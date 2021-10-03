import utils
from mcpi import minecraft

mc = minecraft.Minecraft.create()



from mcpi_utils.wool import setWoolBlock
from mcpi import minecraft
# create a minecraft instace
x, y, z = mc.player.getPos()


blocks = "rrrrryyyyybbbbbgggggoooooyyyyyyyyyyyyyyyyyyyyyyyyuuuuuuuuuuooooooooooooooooo"
England = ["WWRWW",
        "RRRRR",
        "WWRWW"]
France = ["u" * 6 + "W" * 6 + "R" * 6] * 12
Germany = ["BBBBBBBBBB",
           "RRRRRRRRRR",
           "YYYYYYYYYy"]
area=Germany
for dy, element in enumerate(area):
    for dx, colour in enumerate (element):
        setWoolBlock(mc, x+dx, y-dy, z, colour)
    