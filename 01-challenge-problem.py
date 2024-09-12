class Point:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY


class Rectangle:
    def __init__(self, origin, width, height):
        self.starting_point = origin
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def print_coordinates(self):
        top_right = self.starting_point.coordX + self.width
        bottom_left = self.starting_point.coordY + self.height
        print('Starting Point (X)): ' + str(self.starting_point.coordX))
        print('Starting Point (Y)): ' + str(self.starting_point.coordY))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_stuff():
    starting_point = Point(50, 100)
    rect = Rectangle(starting_point, 90, 10)

    return rect


my_rect = build_stuff()

print(my_rect.area())
my_rect.print_coordinates()
