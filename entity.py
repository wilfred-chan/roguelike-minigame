class Entity:
    """
    Usage:
        A generic object to represent players, enimies, items, etc.
    Attributes:
        x(int), y(int): the coordinate of current entity
        char: the character to represent current entity
        color: the color of the character on the console
    """
    def __init__(self, x, y, char, color, name, blocks=False):
        self.x = x
        self.y = y
        self.char = char  # char to present the obj, e.g. @
        self.color = color
        self.name = name
        self.blocks = blocks

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


def get_blocking_entity(entities, target_x, target_y):
    """
    Usage:
        Return the entity which blocks the player's destination point.
    Params:
        entities(list): A list of Entity object.
        target_x, target_y(int): destination coordinates.
    """
    for entity in entities:
        if entity.blocks and (entity.x == target_x and entity.y == target_y):
            return entity
    # If no entity found
    return None