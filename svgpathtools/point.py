__all__ = ["Point"]

import math

class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __abs__(self):
        return type(self)(abs(self.x), abs(self.y))

    def __int__(self):
        return type(self)(int(self.x), int(self.y))

    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)
        
    def __iadd__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return type(self)(self.x - other.x, self.y - other.y)
       
    def __complex__(self):
        return self.x + self.y * 1j
    
    def __isub__(self, other):
        return type(self)(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return type(self)(self.x * other.x, self.y * other.y)
        
    def __imul__(self, other):
        return type(self)(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        return type(self)(self.x / other.x, self.y / other.y)

    def __idiv__(self, other):
        return type(self)(self.x / other.x, self.y / other.y)
    
    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])
        
    def __str__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def scale(self, x_scale, y_scale):
        self.x *= x_scale
        self.y *= y_scale
        
    def scale(self, scale):
        self.x *= scale
        self.y *= scale
    
    def shift(self, x, y):
        self.x += x
        self.y += y
        
    def set(self, x, y):
        self.x = x
        self.y = y
        
    def length(self):
        '''Returns the length of a vector.

        >>> Point(10, 10).length()
        14.142135623730951
        >>> pos = (10, 10)
        >>> Point(pos).length()
        14.142135623730951

        '''
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def lengthSq(self):
        '''Returns the length of a vector squared.

        >>> Point(10, 10).lengthSq()
        200
        >>> pos = (10, 10)
        >>> Point(pos).lengthSq()
        200

        '''
        return self.x ** 2 + self.y ** 2

    def distance(self, to):
        '''Returns the distance between two points.

        >>> Point(10, 10).distance((5, 10))
        5.
        >>> a = (90, 33)
        >>> b = (76, 34)
        >>> Point(a).distance(b)
        14.035668847618199

        '''
        return math.sqrt((self.x - to.x) ** 2 + (self.y - to.y) ** 2)

    def distanceSq(self, to):
        '''Returns the distance between two points squared.

        >>> Point(10, 10).distanceSq((5, 10))
        25

        '''
        return (self.x - to.x) ** 2 + (self.y - to.y) ** 2
    
    def normalize(self):
        '''Returns a new vector that has the same direction as vec,
        but has a length of one.

        >>> v = Point(88, 33).normalize()
        >>> v
        [0.93632917756904444, 0.3511234415883917]
        >>> v.length()
        1.0

        '''
        if self.x == 0. and self.y == 0.:
            return Point(0., 0.)
        return self / self.length()

    def dot(self, a):
        '''Computes the dot product of a and b.

        >>> Point(2, 4).dot((2, 2))
        12

        '''
        return self.x * a.x + self.y * a.y

    def angle(self, a):
        '''Computes the angle between a and b, and return the angle in
        degrees.

        >>> Point(100, 0).angle(Point(0, 100))
        -90.0
        >>> Point(87, 23).angle(Point(-77, 10))
        -157.7920283010705

        '''
        angle = -(180 / math.pi) * math.atan2(
            self.x * a.y - self.y * a.x,
            self.x * a.x + self.y * a.y)
        return angle

    def rotate(self, angle):
        '''Rotate the vector with an angle in degrees.

        >>> v = Point(100, 0)
        >>> v.rotate(45)
        >>> v
        [70.710678118654755, 70.710678118654741]

        '''
        angle = math.radians(angle)
        return Point((self.x * math.cos(angle)) - (self.y * math.sin(angle)),
                      (self.y * math.cos(angle)) + (self.x * math.sin(angle)))