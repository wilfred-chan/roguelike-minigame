from map_objects.tile import Tile
from map_objects.rectangle import Rect


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        # Initialize a 2d array of width * height
        # The initial map is full of walls to prepare for generating man
        tiles = [[Tile(True) for y in range(self.height)]
                 for x in range(self.width)]
        return tiles

    def make_map(self):
        """
        Usage: Call create_room() method to generate rooms(grounds).
        """
        room1 = Rect(20, 15, 20, 10)
        room2 = Rect(30, 20, 10, 20)
        self.create_room(room1)
        self.create_room(room2)

    def create_room(self, room):
        """
        Usage: Creating grounds for the player to walk in the game map.

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
