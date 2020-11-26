class Title:
    """
    A tile obj on a map.
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # block_sight will equal to blocked by default
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight
