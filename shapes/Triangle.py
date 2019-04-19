from shapes.Figure import Figure
import numpy as np

class Triangle(Figure):
    def __init__(self, p, a, b, c):
        super(Triangle, self).__init__(p)
        if a + b <= c or a + c <= b or b + c <= c :
            raise ValueError
        else:
            self._a = a
            self._b = b
            self._c = c
    def get_area(self):
        p = (self._a+self._b+self._c)/2
        return np.sqrt(p*(p-self._a)*(p-self._b)*(p-self._c))
    def get_circut(self):
        return self._a+self._b+self._c