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
        """
        Params:
            x(int), y(int): coordinate of top left corner of the rectangle.
            w(int), h(int): width & height of the rectangle.
        """
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        """
        Usage:
            Return the center point coordinates of a rectangle.
        """
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)
        return center_x, center_y

    def is_intersected(self, other):
        """
        Usage:
            Return True if two rectangles intersect.
        Params:
            other(Rect obj): another rectangle.
        """
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)
