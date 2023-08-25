class Rectangle:
    def __init__(self,widht,height):
        self.widht = widht
        self.height = height 

    def set_width(self, widht):
        self.widht = widht

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.widht * self.height

    def get_perimeter(self):
        return 2 * self.widht + 2 * self.height

    def get_diagonal(self):
        return (self.widht ** 2 + self.height ** 2) ** 0.5


    def get_picture(self):
        if self.widht < 50 and self.height < 50:
            shape = ''
            for i in range(self.height):
                shape += '*' * self.widht + '\n'
            return shape
        else:
            return 'Too big for picture.'

    def get_amount_inside(self, shape):
        a, b = self.get_area() , shape.get_area()
        if a > b:
            return a // b
        return 0 

    def __str__(self):
        return f'Rectangle(width={self.widht}, height={self.height})'

class Square(Rectangle):
    
    def __init__(self,side):
        super().__init__(side,side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
    
    def __str__(self):
        return f'Square(side={self.widht})'


