class Rectangle:
    def __init__(self):
        self.length = int(input("Enter the length of the rectangle:"))
        self.width = int(input("Enter the width of the rectangle:"))

    def perimeter(self):
        peri = 2 * (self.width+ self.length)
        return peri

    def area(self):
        area1 = self.width * self.length
        return area1

    def display(self):
        print(f'The length of the rectangle = {self.length}')
        print(f'The width of the rectangle = {self.width}')
        print(f'The perimeter of the rectangle = {self.perimeter()}')
        print(f'The area of the rectangle = {self.area()}')


class Parallelepipede(Rectangle):
    def __init__(self):
        Rectangle.__init__(self)
        self.height = int(input("Enter the height if the parallelepipede:"))

    def volume(self):
        vol = self.width * self.length * self.length
        return vol


rec= Rectangle()
rec.display()
