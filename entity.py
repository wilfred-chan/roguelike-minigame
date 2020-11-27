class Entity:
    """
    Usage:
        A generic object to represent players, enimies, items, etc.
    Attributes:
        x(int), y(int): the coordinate of current entity
        char: the character to represent current entity
        color: the color of the character on the console
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char  # char to present the obj, e.g. @
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
