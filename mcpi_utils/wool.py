from mcpi import block

# Wool Colours
WHITE = 0
ORANGE = 1
MAGENTA = 2
LIGHT_BLUE = 3
YELLOW = 4
LIME = 5
PINK = 6
GREY = 7
LIGHT_GREY = 8
CYAN = 9
PURPLE = 10
BLUE = 11
BROWN = 12
GREEN = 13
RED = 14
BLACK = 15

wool_types = {"A": BROWN,
              "B": BLACK,
              "C": CYAN,
              "G": GREEN,
              "H": GREY,
              "I": LIGHT_GREY,
              "L": LIME,
              "M": MAGENTA,
              "O": ORANGE,
              "P": PINK,
              "Q": PURPLE,
              "R": RED,
              "U": BLUE,
              "V": LIGHT_BLUE,
              "W": WHITE,
              "Y": YELLOW}

def setWoolBlock(mc, x, y, z, type=WHITE):
    """
    Create a wool block of the specified colour in the specified position

    'type' is either an integer corresponding to the data ID or a character
    from the wool_types dict
    """
    try:
        c = wool_types[type.upper()]
    except:
        c = type

    mc.setBlock(x, y, z, block.WOOL.id, c)
