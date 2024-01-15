#!/usr/bin/python3
"""import Rectangle class"""


from models.rectangle import Rectangle


"""square classe (inherite from Rectangle)"""


class Square(Rectangle):
    """square classe (inherite from Rectangle)"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of a Square"""
        return (f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """property size"""
        return (self.height)

    @size.setter
    def size(self, value):
        """property setter size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class Square"""
        if args:
            if (len(args)) >= 1:
                self.id = args[0]
            if (len(args)) >= 2:
                self.size = args[1]
            if (len(args)) >= 3:
                self.x = args[2]
            if (len(args)) >= 4:
                self.y = args[3]

        elif kwargs:
            the_keys = ['id', 'size', 'x', 'y']
            for key, value in kwargs.items():
                if key in the_keys:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Square instance to dictionary representation"""
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
