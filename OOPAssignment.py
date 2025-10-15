# OOP Assignment
# create base clase called Shape
# create child classes called Circle, Triangle, Rectangle
# for each shape/class find area and perimeter
import math

PI = math.pi


class Shape:

    def print_results(self):
        print(self.name, "area =", self.area)
        print(self.name, "perimeter =", self.perimeter)
    
class Triangle(Shape):
    name = "Triangle"

    def calc_area_triangle(self, side_a, side_b, side_c):
        semi_perimeter = (side_a + side_b + side_c) / 2
        area = math.sqrt((semi_perimeter * (semi_perimeter - side_a) *
                          (semi_perimeter - side_b) *
                          (semi_perimeter - side_c)))
        self.area = area
        return area

    def calc_perimeter_triangle(self, side_a, side_b, side_c):
        perimeter = side_a + side_b + side_c
        self.perimeter = perimeter
        return perimeter

    def calc(self, side_a, side_b, side_c):
        self.calc_area_triangle(side_a, side_b, side_c)
        self.calc_perimeter_triangle(side_a, side_b, side_c)

class Rectangle(Shape):
    name = "Rectangle"

    def calc_area_rectangle(self, height, width):
        area = height * width
        self.area = area
        return area

    def calc_perimeter_rectangle(self, height, width):
        perimeter = 2 * height + 2 * width
        self.perimeter = perimeter
        return perimeter

    def calc(self, height, width):
        self.calc_area_rectangle(height, width)
        self.calc_perimeter_rectangle(height, width)

class Circle(Shape):
    name = "Circle"

    def calc_area_circle(self, radius):
        area = PI * radius ** 2
        self.area = area
        return area

    def calc_perimeter_circle(self, radius):
        perimeter = 2 * PI * radius
        self.perimeter = perimeter
        return perimeter

    def calc(self, radius):
        self.calc_area_circle(radius)
        self.calc_perimeter_circle(radius)

triangle = Triangle()
rectangle = Rectangle()
circle = Circle()

circle.calc(1)
circle.print_results()
rectangle.calc(1, 1)
rectangle.print_results()
triangle.calc(1, 1, 1)
triangle.print_results()
