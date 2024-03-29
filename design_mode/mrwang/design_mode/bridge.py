# -*- coding:utf-8 -*-

# concreteImplementor 1/2
class DrawingAPI(object):
    def draw_circle(self, x, y, radius):
        print("API1.circle at {}:{} radius {}".format(x, y, radius))

#concreteImplementor 2/2
class DrawingaPI2(object):
    def draw_circle(self, x, y, radius):
        print("API2.circle at {}:{} radius {}".format(x, y, radius))

# refined abstraction
class Circleshap(object):
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    # low-level i.e Implementation specific
    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._drawing_api)

    # high_levle i.e Abstraction specific
    def scale(self, pct):
        self._radius *= pct

def main():
    shapes = {
        Circleshap(1, 2, 3, DrawingAPI()),
        Circleshap(5, 7, 11, DrawingaPI2())
    }

    for shape in shapes:
        shape.scale(2.5)
        shape.draw()


if __name__ == "__main__":
    main()