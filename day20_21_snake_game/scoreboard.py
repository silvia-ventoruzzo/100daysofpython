from turtle import Turtle
ALIGNMENT = 'CENTER'
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    '''
    Class to keep track of score, i.e. number of times snake eats food.
    '''
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.setposition(x=0, y=275)
        self.show()
        self.hideturtle()
        
    def show(self): 
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)   
        
    def increase(self):
        self.score += 1
        self.clear()
        self.show()
        
    def game_over(self):
        self.setposition(x=0, y=0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)