#
# pictures.py - Image manipuation tools to translate pictures into
#               minecraft blocks

# PIL is an image processing library for Python
from PIL import Image

from mcpi_utils.wool import setWoolBlock, wool_pallete, WoolColors

MAX_SIZE = 64

def customConvert(silf, palette, dither=False):
    ''' 
    Convert the colours of an image to the closest available colour from the 
    given palette. PIL provifes the quantize function to do this, but it uses
    dither - an attempt to simulate missing colours by mixing in pixels of colours.

    This looks rubbish in a 64-pixel image and it cannot be turned off so we
    have to write our own colour convrsion function (or copy one from stackoverflow)
    
    https://stackoverflow.com/questions/29433243/convert-image-to-specific-palette-using-pil-without-dithering
    '''

    silf.load()

    # use palette from reference image made below
    palette.load()
    im = silf.im.convert("P", 0, palette.im)
    # the 0 above means turn OFF dithering making solid colors
    return silf._new(im)


def image_to_mc_colors(image):
    """
    Replace all the colours in the image with the closest minecraft colour.
    Each pixel in the image is replaced with an integer corresponding to one
    of the colours in the pallete. 
    
    In this case we are using wool blocks and the colour is the data ID of the
    wool block of the appropriate colour in minecraft.
    """
    pal_image= Image.new("P", (1,1))
    pal_image.putpalette(wool_pallete())
    return customConvert(image.convert("RGB"), pal_image)


def image_to_pixels(image, max_size):
    """
    Read an image, resize it to the specified number of pixels
    then return a list of lists of pixels
    """
    with Image.open(image) as image:
        # The 'thumbnail' funcction resizes the image to the specified number
        # of pixels in its longest dimension
        image.thumbnail((max_size, max_size))
        max_x, max_y = image.size

        # Now convert the colours in the image to the closest value in the set 
        # we have available.
        converted_image = image_to_mc_colors(image)

        # Finally loop through the image and create a 2-dimensional list (a list
        # of lists) of pixels. 
        result = []
        for y in range(max_y):
            result.append([])
            for x in range(max_x):
                # If the original pixel was transparent then use 255
                # Otherwise use the color from the converted image
                old_pixel = image.getpixel((x,y))
                new_pixel = converted_image.getpixel((x,y))
                if (old_pixel[3] == 0):
                    # Alpha of 0, so transparent
                    result[y].append(255)
                else:
                    result[y].append(new_pixel)

    return result


def build_pixels(mc, pixels, x, y, z):
    """
    Take a list of lists of pixels and build them in a minecraft instance
    """
    # Start from the top and build downwards.
    start_y = y + len(pixels)
    # Center the image horizontally from the given start position
    start_x = int(x - 0.5 * len(pixels[0]))
    
    # For each pixel create a minecraft block in the corresponding position 
    for dy, row in enumerate(pixels):
        for dx, pixel in enumerate(row):
            if pixel >= len(WoolColors):
                mc.setBlock(start_x + dx, start_y - dy, z, 0)
            else:
                setWoolBlock(mc, start_x + dx, start_y - dy, z, pixel)


def build_image(mc, x, y, z, image_file, max_size=MAX_SIZE):
    """
    Load an image and build it in a minecraft world
    """

    # Convert the image into the right size and colours
    pixels = image_to_pixels(image_file, max_size)

    # Build the pixels in the minecraft instance
    build_pixels(mc, pixels, x, y, z)
