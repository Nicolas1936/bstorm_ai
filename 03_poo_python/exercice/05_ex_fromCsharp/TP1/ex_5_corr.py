class Point:

    def __init__(self, x, y = None, z = None):
        
        self.x = x
        self.y = y
        self.z = z

    def translate(self, x, y = None, z = None):

        self.x += x

        if y is not None and self.y is not None:
            self.y += y

        if z is not None and self.z is not None:
            self.z += z

    def __str__(self):
        return f"({self.x}; {self.y}; {self.z})"