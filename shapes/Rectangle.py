from shapes.Square import Square,Point

class Rectangle(Square):
    def __init__(self, p, a, b):
        super(Rectangle,self).__init__(p, a)
        self._b = b

    def get_area(self):
        return self._a*self._b

    def get_circut(self):
        return self._a*2 + self._b*2