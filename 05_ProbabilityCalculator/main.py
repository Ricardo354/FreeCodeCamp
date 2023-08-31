import random
import copy

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
    count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_gotten = hat.copy.draw(num_balls_drawn)
        new_colors = [i for i, j in expected_copy.items() for _ in range(j)]
        if colors_gotten == new_colors:
            count += 1
    return count / num_experiments



        


    

