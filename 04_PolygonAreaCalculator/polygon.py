class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height 

    def set_width(self, width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5


    def get_picture(self):
        if self.width < 50 or self.height < 50:
            shape = ''
            for i in range(self.height):
                shape += '*' * self.width + '\n'
            return shape
        else:
            return 'Too big for picture.'

    def get_amount_inside(self, shape):
        a, b = self.get_area() , shape.get_area()
        if a > b:
            return a // b
        return 0 

    def __str__(self):
        return f'Rectangle(widht={self.width}, height={self.height})'

class Square(Rectangle):
    
    def __init__(self,side):
        super().__init__(side,side)

    