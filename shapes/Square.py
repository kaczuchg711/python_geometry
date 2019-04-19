from shapes import Figure, Point


class Square(Figure.Figure):
    def __init__(self, p: Point, a: float):
        super(Square,self).__init__(p)
        self._a = a

    def get_area(self):
        return self._a**2

    def get_circut(self):
        return a*4