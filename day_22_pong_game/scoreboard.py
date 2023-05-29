from turtle import Turtle
ALIGNMENT = 'CENTER'
FONT = ('Courier', 28, 'normal')

class Scoreboard(Turtle):
    '''
    Class to keep track of score
    '''
    
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.color('white')
        self.setposition(x=0, y=270)
        self.show()
        self.hideturtle()
        
    def show(self): 
        self.write(f'{self.l_score} - {self.r_score}', align=ALIGNMENT, font=FONT)   
        
    def increase(self, side):
        if side == 'left':
            self.l_score += 1
        elif side == 'right':
            self.r_score += 1
        self.clear()
        self.show()