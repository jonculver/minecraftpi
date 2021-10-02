from PIL import Image

from mcpi_utils.wool import setWoolBlock, color_to_rgb, WoolColors

MAX_SIZE = 64

def customConvert(silf, palette, dither=False):
    ''' Convert an RGB or L mode image to use a given P image's palette.
        PIL.Image.quantize() forces dither = 1. 
        This custom quantize function will force it to 0.
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
    Replace all the colours in the image with the closest minecraft colour
    (Each pixel in the image will be an integer corresponding to a WoolColor value, or
     larger if none)
    """
    pal_image= Image.new("P", (1,1))
    pal_image.putpalette([c for color in WoolColors for c in color_to_rgb(color)] + [0,0,0] * (256 - len(WoolColors) - 1))
    return customConvert(image.convert("RGB"), pal_image)

def image_to_pixels(image, max_size):
    """
    Read an image, resize it to the specified number of pixels
    then return a list of lists of pixels
    """
    with Image.open(image) as image:
        image.thumbnail((max_size, max_size))
        max_x, max_y = image.size
        converted_image = image_to_mc_colors(image)
        result = []
        for y in range(max_y):
            result.append([])
            for x in range(max_x):
                # If the original pixel was transparent then use 255
                # Otherwise use the color from the converted image
                old_pixel = image.getpixel((x,y))
                new_pixel = converted_image.getpixel((x,y))
                if (old_pixel[3] == 0):
                    # Alpha of 0 so transparent
                    result[y].append(255)
                else:
                    result[y].append(new_pixel)

        return result


def build_pixels(mc, pixels, x, y, z):
    """
    Take a list of lists of pixels and build them in a minecraft instance
    """
    # Start at the top
    start_y = y + len(pixels)
    start_x = int(x - 0.5 * len(pixels[0]))

    for dy, row in enumerate(pixels):
        for dx, pixel in enumerate(row):
            if pixel >= len(WoolColors):
                mc.setBlock(start_x + dx, start_y - dy, z, 0)
            else:
                setWoolBlock(mc, start_x + dx, start_y - dy, z, pixel)


def build_image(mc, image_file, max_size=MAX_SIZE):
    """
    Load an image and build it in a minecraft world
    """
    
    # Find the player location and set the start location to be a short distance away
    x, y, z = mc.player.getPos()
    z -= 10

    pixels = image_to_pixels(image_file, max_size)
    build_pixels(mc, pixels, x, y, z)
