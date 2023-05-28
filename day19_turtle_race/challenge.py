# Make a etch-a-sketch app

from turtle import Turtle, Screen

sketch = Turtle()
screen = Screen()

def forwards():
    sketch.forward(10)
    
def backwards():
    sketch.backward(10)
    
def counterclockwise():
    sketch.left(10)
    
def clockwise():
    sketch.right(10)
    
def clear():
    sketch.reset()
    
screen.listen()
screen.onkeypress(fun=forwards, key='w')
screen.onkeypress(fun=backwards, key='s')
screen.onkeypress(fun=counterclockwise, key='a')
screen.onkeypress(fun=clockwise, key='d')
screen.onkeypress(fun=clear, key='c')

screen.exitonclick()