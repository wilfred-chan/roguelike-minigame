from map_objects.tile import Tile
from map_objects.rectangle import Rect


class GameMap:
    """
    Usage:
        Build a GameMap object.
    Attributes:
        width(int), height(int).
    """
    def __init__(self, width, height):
        """
        Usage:
            Initialize the GameMap object with full of wall tiles.
        Params:
            width(int), height(int).
        """
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        """
        Usage:
            Initialize tiles in the map, via a 2d array of width * height.
            Return a 2d array of Tile objects.
        """
        # The initial map is full of walls
        # to prepare for generating rooms(grounds)
        tiles = [[Tile(True) for y in range(self.height)]
                 for x in range(self.width)]
        return tiles

    def make_map(self):
        """
        Usage: Call create_room() method to generate rooms(grounds).
        """
        room1 = Rect(25, 15, 20, 15)
        room2 = Rect(45, 20, 20, 25)
        room3 = Rect(5, 5, 40, 10)
        room4 = Rect(5, 25, 10, 20)
        room5 = Rect(70, 20, 10, 25)
        room6 = Rect(30, 5, 10, 10)
        self.create_room(room1)
        self.create_room(room2)
        self.create_room(room3)
        self.create_room(room4)
        self.create_room(room5)
        self.create_room(room6)

    def create_room(self, room):
        """
        Usage:
            Create a room for the player to walk in the game map.
        Params:
            room: a Rect object from map_objects.rectangle.
        """
        # carve out a walkable rectangle (inner) in the map of walls
        # reason why don't add 1 to x2 & y2 is because
        # range(,) is exclusive for latter param
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        """
        Usage:
            Return True if the tiles[x][y] is blocked.
        Params:
            x(int): x coordinate in GameMap.tiles.
            y(int): y coordinate in GameMap.tiles.
        """
        if self.tiles[x][y].blocked:
            return True
        else:
            return False
