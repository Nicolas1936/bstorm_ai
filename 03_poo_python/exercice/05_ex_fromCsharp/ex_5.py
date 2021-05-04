class Point:
    #INITIALISATION
    def __init__(self, x, y=None, z=None):
        self.x = x
        if y is not None:
            self.y = y
        else:
            self.y = x

        if z is not None:
            self.z = z
        else:
            self.z = x

    def __str__(self):
        return "x : {}, y : {}, z : {}".\
            format(self.x, self.y, self.z)

    def translate(self, x=None, y=None, z=None):
        if x is not None:
            self.x += x
        if y is not None:
            self.y += y 
        if z is not None:
            self.z += z 

if __name__ == '__main__':
    
    p = Point(3)
    print(p)

    p1 = Point(3, 2)
    print(p1)

    p2 = Point(3, 2, 1)
    print(p2)

    p2.translate(4, 7, 4)
    print(p2)