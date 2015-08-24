import math

class Vect2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt(self.dist2(other))

    def dist2(self, other):
        return (other.x - self.x)**2 + (self.y - other.y)**2

    def dot(self, other):
        return self.x*other.x + self.y*other.y
        
    def normalise(self):
        return self / abs(self)

    def limit(self, maximum = None, minimum = None):
        norm2 = self.dot(self)
        if maximum and norm2 > maximum**2:
            self *= maximum / math.sqrt(norm2)
        elif minimum and norm2 < minimum**2:
            self *= minimum / math.sqrt(norm2)
    
    def __repr__(self):
        return "Vect2D("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
        
    def __add__(self, other):
        return Vect2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vect2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vect2D(self.x * other, self.y * other)

    def __rmul__(self, other):
        return Vect2D(self.x * other, self.y * other)

    def __div__(self, other):
        return Vect2D(self.x / other, self.y / other)

    def __truediv__(self, other):
        return Vect2D(self.x / other, self.y / other)

    def __floordiv__(self, other):
        return Vect2D(self.x // other, self.y // other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    
    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self
    
    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        return self
    
    def __ifloordiv__(self, other):
        self.x //= other
        self.y //= other
        return self

    def __neg__(self):
        return Vect2D(-self.x, -self.y)

class Vect:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def dist(self, other):
        return math.sqrt(self.dist2(other))

    def dist2(self, other):
        return (other.x - self.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2
        
    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def normalise(self):
        return self / abs(self)

    def limit(self, maximum = None, minimum = None):
        norm2 = self.dot(self)
        if maximum and norm2 > maximum**2:
            self *= maximum / math.sqrt(norm2)
        elif minimum and norm2 < minimum**2:
            self *= minimum / math.sqrt(norm2)
    
    def __repr__(self):
        return "Vect("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
        
    def __add__(self, other):
        return Vect(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vect(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vect(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return Vect(self.x * other, self.y * other, self.z * other)

    def __div__(self, other):
        return Vect(self.x / other, self.y / other, self.z / other)

    def __truediv__(self, other):
        return Vect(self.x / other, self.y / other, self.z / other)

    def __floordiv__(self, other):
        return Vect(self.x // other, self.y // other, self.z // other)

    # def __iadd__(self, other):
    #     self.x += other.x
    #     self.y += other.y
    #     self.z += other.z
    #     return self

    # def __isub__(self, other):
    #     self.x -= other.x
    #     self.y -= other.y
    #     self.z -= other.z
    #     return self
    
    # def __imul__(self, other):
    #     self.x *= other
    #     self.y *= other
    #     self.z *= other
    #     return self
    
    # def __itruediv__(self, other):
    #     self.x /= other
    #     self.y /= other
    #     self.z /= other
    #     return self
    
    # def __ifloordiv__(self, other):
    #     self.x //= other
    #     self.y //= other
    #     self.z //= other
    #     return self

    def __neg__(self):
        return Vect(-self.x, -self.y, -self.z)
