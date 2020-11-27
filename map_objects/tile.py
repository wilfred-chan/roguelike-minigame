class Tile:
    """
    Usage:
        A tile obj on a map.
    Attributes:
        blocked(bool): True if the tile is blocked
        block_sight(bool): Default value is None,
        True if the tile blocks sight.
    """
    def __init__(self, blocked, block_sight=None):
        """
        Usage:
            Construct the attributes of Tile class.
        Params:
            blocked(bool): True if the tile is blocked
            block_sight(bool): Default value is None,
            but will be initialized to be same with blocked(bool).
        """
        self.blocked = blocked
        # block_sight will equal to blocked by default
        if block_sight is None:
            block_sight = blocked
        self.block_sight = block_sight
        self.explored = False
