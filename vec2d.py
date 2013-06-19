class Vec2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __add__(self, param):
        return Vec2D(self._x + param.x, self._y + param.y)

    def __sub__(self, param):
        return Vec2D(self._x - param.x, self._y - param.y)

    def __mul__(self, number):
        return Vec2D(self._x * number, self._y * number)

    def __eq__(self, vector):
        return type(vector) is Vec2D and (self._x, self._y) == tuple(vector)

    def __neg__(self):
        return Vec2D(-self._x, -self._y)

    def __iter__(self):
        return iter([self._x, self._y])
