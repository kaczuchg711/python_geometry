from shapes import Point
# trzeba używać NazwaKlasy.soś

class Figure:
    def __init__(self, p: Point):
        self._p = p


p = Point.Point(1, 2)

f = Figure(p)

print(f._p)

