import math


class Figure:

    def __init__(self):
        self.area = None

    def __add__(self, other):
        new_figure = self.__class__
        new_figure.area = self.area + other.area
        return new_figure.area

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area

    def __le__(self, other):
        return self.area <= other.area

    def __gt__(self, other):
        return self.area > other.area

    def __ge__(self, other):
        return self.area >= other.area


class Circle(Figure):
    def __init__(self, radius=1):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self._radius = value

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return self.radius ** 2 * math.pi

    @area.setter
    def area(self, value):
        self.radius = math.sqrt(value / math.pi)


class Square(Figure):
    def __init__(self, side=1):
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @area.setter
    def area(self, area):
        self.side = math.sqrt(area)


class Triangle(Figure):
    def __init__(self, base=1, height=3):
        self.base = base
        self.height = height

    @property
    def area(self):
        return self.base * self.height / 2

    @area.setter
    def area(self, value):
        self._area = value



circle = Circle(5)
# print(okrąg.radius)
# print(okrąg.diameter)
# print(okrąg.area)
# okrąg.radius = 5
# print(okrąg.diameter)
# print(okrąg.area)
# print()
# okrąg.diameter = 12
# print(okrąg.radius)
# print(okrąg.area)
# print()
# okrąg.area = 78.53981633974483
# print(okrąg.radius)
# print(okrąg.diameter)

# print(circle.radius)
# circle.radius = 5
# print(circle.radius)
# circle.radius = 2
# print(circle.radius)
# c1 = Circle(1)
c2 = Circle(2)
# print(c1 == c2)
# print(c1 > c2)
# print(c1 <= c2)
#
# print()
#
k1 = Square(5)
k2 = Square(10)
#
# print()
# print(k1 == k2)
# print(k1 > k2)
# print(k1 <= k2)
# print(k1 + c2)

print()
t = Triangle(5)


print(t.height)
print(t.area)
print(t.base)
print()
print(t == k2)
print(t > k2)
print(t <= k2)
print(t + c2)
