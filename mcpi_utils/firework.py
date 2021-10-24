from mcpi import block
from random import randint
from minecraftstuff import MinecraftDrawing


class Firework():

    MAX_RADIUS = 8

    def __init__(self, mc, x, y, z):
        """
        Create a new firework at coordinates x, y, z
        """

        self.mc = mc
        self.draw = MinecraftDrawing(mc)
        self.x = x
        # Start on the ground
        self.y = mc.getHeight(x, z) + 1
        self.z = z
        self.draw_rocket()
        self.height = randint(15, 25)
        self.radius = 2
        self.color = randint(0,14)

    def draw_rocket(self):
        """
        Draw the rocket at the current coordinates
        """
        self.mc.setBlock(self.x, self.y + 2, self.z, block.TNT, 1)
        self.mc.setBlocks(self.x, self.y, self.z,
                          self.x, self.y + 1, self.z, block.FENCE)

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
        if self.height > 0:
            self.launch()            
        elif self.radius < self.MAX_RADIUS:
            self.explode()

    def finished(self):
        """
        Returns true if this firework is finished exploding, otherwise false
        """
        return self.radius == self.MAX_RADIUS           
