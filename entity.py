import math


class Entity:
    """
    Usage:
        A generic object to represent players, enimies, items, etc.
    Attributes:
        x(int), y(int): the coordinate of current entity
        char(str): the character to represent current entity
        color(tcod.color): the color of the character on the console
        name(str): the name of the entity
        blocks(bool): default as False, True if the entity can block players
        fighter(Fighter obj): a Fighter object from components.
        ai(BasicMonster obj): a BasicMonster object from components.
    """
    def __init__(
        self, x, y, char, color, name, blocks=False, fighter=None, ai=None
    ):
        self.x = x
        self.y = y
        self.char = char  # char to present the obj, e.g. @
        self.color = color
        self.name = name
        self.blocks = blocks
        self.fighter = fighter
        self.ai = ai

        if self.fighter:
            self.fighter.owner = self
        if self.ai:
            self.ai.owner = self

    def move(self, dx, dy):
        # for player
        self.x += dx
        self.y += dy

    def move_toward(self, target, game_map, entities):
        """
        Usage:
            Move toward the target entity.
        Params:
            target(Entity obj)
            game_map(GameMap obj)
            entities(list)
        """
        # for enemies
        diff_x = target.x - self.x
        diff_y = target.y - self.y
        dx, dy = (0, 0)
        if diff_x < -1:
            dx = -1
        elif diff_x > 1:
            dx = 1
        if diff_y < -1:
            dy = -1
        elif diff_y > 1:
            dy = 1
        if not (
            game_map.is_blocked(self.x + dx, self.y + dy) or
            get_blocking_entity(entities, self.x + dx, self.y + dy)
        ):
            self.move(dx, dy)

    def get_distance(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)


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