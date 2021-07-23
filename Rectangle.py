class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

my_rectangle = Rectangle(4, 3)

print(my_rectangle.area())
