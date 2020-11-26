class Entity:
    """
    A generic object to represent players, enimies, items, etc.
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char  # char to present the obj, e.g. @
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
