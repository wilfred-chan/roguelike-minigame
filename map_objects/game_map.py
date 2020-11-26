from map_objects.tile import Tile


class GameMap:
    def __init__(self, width, height):
        """
        docstring
        """
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        # Initialize a 2d array of width * height
        tiles = [[Tile(False) for y in range(self.height)] for x in range(self.width)]

        # for demonstration purpose only
        tiles[30][22].blocked = True
        tiles[30][22].block_sight = True
        tiles[31][22].blocked = True
        tiles[31][22].block_sight = True
        tiles[32][22].blocked = True
        tiles[32][22].block_sight = True

        return tiles

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True
        else:
            return False
