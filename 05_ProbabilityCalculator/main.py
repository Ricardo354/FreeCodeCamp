import random


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
         
    def draw(self, n): # RETURNS RANDOM LIST WITH n BALLS
        balls = []
        if n <= len(self.contents):
            for i in range(n):
                choice = self.contents.pop(int(random.random()* len(self.contents)))
                balls.append(choice)
            return balls
        else:
            return self.contents



  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat = hat
    for i in range(num_experiments):
        Hat.draw(hat, num_balls_drawn)

    

