class Rect:
    """
    Usage:
        A rectangle object, for game map generating.
    Params:
        x(int), y(int): coordinate of the top left corner
        w(int): width of rectangle
        h(int): height of rectangle
    Attributes:
        x1, y1(int): coordinate of the top left corner
        x2, y2(int): coordinate of the bottom right corner
    """
    def __init__(self, x, y, w, h):
        # x and y are the coordinates
        # of the top left corner of the rectangle
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

