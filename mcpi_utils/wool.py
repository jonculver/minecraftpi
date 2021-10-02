from mcpi import block
from enum import IntEnum
# Wool Colours

# Enumeration of wool colours with values corresponding to the
# data ID of the block
class WoolColors(IntEnum):
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


# Mapping from letters to wool colors
wool_types = {"A": WoolColors.BROWN,
              "B": WoolColors.BLACK,
              "C": WoolColors.CYAN,
              "G": WoolColors.GREEN,
              "H": WoolColors.GREY,
              "I": WoolColors.LIGHT_GREY,
              "L": WoolColors.LIME,
              "M": WoolColors.MAGENTA,
              "O": WoolColors.ORANGE,
              "P": WoolColors.PINK,
              "Q": WoolColors.PURPLE,
              "R": WoolColors.RED,
              "U": WoolColors.BLUE,
              "V": WoolColors.LIGHT_BLUE,
              "W": WoolColors.WHITE,
              "Y": WoolColors.YELLOW}
# Mapping from wool colours to RGB values
wool_rgb = {WoolColors.BROWN      : (59,  35,  19 ), 
            WoolColors.BLACK      : (0,   0,   0  ), 
            WoolColors.CYAN       : (27,  78,  101), 
            WoolColors.GREEN      : (41,  135,  18 ), 
            WoolColors.GREY       : (45,  45,  45 ), 
            WoolColors.LIGHT_GREY : (116, 116, 116), 
            WoolColors.LIME       : (86,  146, 37 ), 
            WoolColors.MAGENTA    : (124, 38,  131), 
            WoolColors.ORANGE     : (169, 96,  46 ), 
            WoolColors.PINK       : (160, 106, 121), 
            WoolColors.PURPLE     : (92,  35,  142), 
            WoolColors.RED        : (135, 37,  34 ), 
            WoolColors.BLUE       : (27,  36,  110), 
            WoolColors.LIGHT_BLUE : (76,  101, 153), 
            WoolColors.WHITE      : (200, 200, 200), 
            WoolColors.YELLOW     : (147, 136, 12 )}


def id_from_letter(letter):
    """
    Return the colour corresponding to a letter or None if not recognised
    """
    result = None
    upper = letter.upper()
    if upper in wool_types:
        result = wool_types[upper]
    return result


def color_to_rgb(color):
    """
    Return the RGB value of a color
    """
    result = None
    if color in wool_rgb:
        result = wool_rgb[color]
    return result


def setWoolBlock(mc, x, y, z, color=WoolColors.WHITE):
    """
    Create a wool block of the specified colour in the specified position

    'type' is either a WoolColor enum value or a letter
    """
    c = None
    try:
        c = id_from_letter(color)
    except:
        pass

    if c is None:
        c = color

    if c is not None:
        mc.setBlock(x, y, z, block.WOOL.id, c)
    else:
        mc.setBlock(x, y, z, 0)
