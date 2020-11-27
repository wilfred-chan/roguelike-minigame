from map_objects.tile import Tile
from map_objects.rectangle import Rect
from random import randint


class GameMap:
    """
    Usage:
        Build a GameMap object.
    Attributes:
        width(int), height(int).
        tiles(list): sample tiles (2d array) below.
        [
            |-------------------height(y)----------------|  ___
           0[Tile(..),Tile(..),Tile(..),Tile(..),Tile(..)]   |
           1[Tile(..),Tile(..),Tile(..),Tile(..),Tile(..)], width(x)
           2[Tile(..),Tile(..),Tile(..),Tile(..),Tile(..)], _|_
        ]      0        1        2        3        4
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

    def make_map(self, player):
        """
        Usage:
            Generate inter-connected rooms.
        Param:
            player(Entity obj): an Entity object to be updated with
            initial position of player
        """
        rooms_created = []
        # Generating rooms
        for rm in range(15+1):  # Generate 15 rooms (if no intersection)
            # random width & height
            w = randint(5, 20)
            h = randint(5, 20)
            # random left-top point
            x = randint(1, self.width - w - 1)
            y = randint(1, self.height - h - 1)
            new_room = Rect(x, y, w, h)
            intersection_count = 0
            for other_room in rooms_created:
                if new_room.is_intersected(other_room):
                    intersection_count += 1
            if intersection_count == 0:
                self.create_room(new_room)
                rooms_created.append(new_room)
        # Update player's initial positioa
        player.x, player.y = rooms_created[0].center()
        # Generating rooms
        for idx in range(len(rooms_created)):
            if idx == (len(rooms_created) - 1):
                self.connect_rooms(rooms_created[idx], rooms_created[0])
            else:
                self.connect_rooms(rooms_created[idx], rooms_created[idx+1])

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

    def connect_rooms(self, room1, room2):
        """
        Usage:
            Creating tunnels between two rooms.
        Params:
            room1, room2(Rect obj): two non-intersected Rect objects.
        """
        room1_center_x, room1_center_y = room1.center()
        room2_center_x, room2_center_y = room2.center()
        order = randint(0, 1)
        if order == 0:
            self.create_horizontal_tunnel(room1_center_x, room2_center_x,
                                          room1_center_y)
            self.create_vertical_tunnel(room1_center_y, room2_center_y,
                                        room2_center_x)
        else:
            self.create_vertical_tunnel(room1_center_y, room2_center_y,
                                        room1_center_x)
            self.create_horizontal_tunnel(room1_center_x, room2_center_x,
                                          room2_center_y)

    def create_horizontal_tunnel(self, x1, x2, y):
        """
        Usage:
            Create horizontal tunnels between rectangles.
        Params:
            x1, x2(int): two coordinates of width.
            y(int): the coordinate of height.
        """
        if x1 > x2:
            temp = x1
            x1 = x2
            x2 = temp
        for x in range(x1, x2+1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_vertical_tunnel(self, y1, y2, x):
        """
        Usage:
            Create vertical tunnels between rectangles.
        Params:
            y1, y2(int): two coordinates of width.
            x(int): the coordinate of height.
        """
        if y1 > y2:
            temp = y1
            y1 = y2
            y2 = temp
        for y in range(y1, y2+1):
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
