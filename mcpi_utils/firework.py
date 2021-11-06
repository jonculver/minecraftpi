from mcpi import block
from random import randint
from minecraftstuff import MinecraftDrawing
from mcpi_utils.wool import parse_color


class Firework():

    MAX_RADIUS = 8

    def __init__(self, mc, x, z, delay=0, color=None, height=None):
        """
        Create a new Firework object on the ground at the specified X and Z coordinates

        Args:
            mc: Minecraft instance in which to create the firework
            x (int): X coordinate of firework
            z (int): Z coordinate of firework
            delay (int, optional): How many ticks to wait before launching. Defaults to 0.
            color (int or char, optional): Either an integer less than 14 or a letter code. Defaults to random.
            height (int, optional): The height off the ground to explode. Defaults to random between 20 and 25.
        """

        self.mc = mc
        self.draw = MinecraftDrawing(mc)
        self.x = x
        # Start on the ground
        self.y = mc.getHeight(x, z) + 1
        self.z = z
        self.delay = delay
        self.draw_rocket()
        if height is not None:
            self.height = height
        else:
            self.height = randint(20, 25)
        self.radius = 2
        if color is not None:
            self.color = parse_color(color)
        else:
            self.color = randint(0,14)

    def draw_rocket(self):
        """
        Draw the rocket at the current coordinates
        """
        self.mc.setBlock(self.x, self.y + 2, self.z, block.TNT.id, 1)
        self.mc.setBlocks(self.x, self.y, self.z,
                          self.x, self.y + 1, self.z, block.FENCE.id)

    def launch(self):
        """
        Move the rocket up one space and update the coordinates. If it reaches the top then start exploding

        """
        # Move the rocket up one space
        self.mc.setBlock(self.x, self.y, self.z, 0)
        self.y += 1
        self.draw_rocket()
        self.height -= 1
        # If we've reached the top then explode
        if self.height == 0:
            self.mc.setBlocks(self.x, self.y, self.z, self.x, self.y+2, self.z, 0)
            self.y += 2
            self.explode()

    def explode(self):
        """
        Clear any existing explosion, increase the radius by 1 and draw a circle
        """
        self.draw.drawHorizontalCircle(self.x, self.y, self.z, self.radius, 0)
        self.radius += 1
        if self.radius < self.MAX_RADIUS:
            self.draw.drawHorizontalCircle(self.x, self.y, self.z, self.radius, block.WOOL.id, self.color)

    def move(self):
        """
        Advance the firework by one tick, either launching or exploding
        """
        if self.delay > 0:
            self.delay -= 1
        elif self.height > 0:
            self.launch()            
        elif self.radius < self.MAX_RADIUS:
            self.explode()

    def finished(self):
        """
        Returns true if this firework is finished exploding, otherwise false
        """
        return self.radius == self.MAX_RADIUS           
