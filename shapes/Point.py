class Point:
    def __init__(self, x: float, y: float, name: str = "no name"):
        self._x = x
        self._y = y
        self._name = name

    def __str__(self):
        return '(' + self._x.__str__() + ',' + self._y.__str__() + ')' + ' "' + self._name + '"'

    def show(self):
        print(self.get_x(), self.get_y(), self.get_name())

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_name(self, name):
        self._name = name

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_name(self):
        return self._name
