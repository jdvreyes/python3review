# spirale_0.py is a infinite recursive function
from turtle import *

# infinite recursive function
def spirale(x):
    forward(x)
    right(90)
    spirale(0.9*x) #recursive call
    return

def spiral(x):
    if x < 5:
        return
    else:
        forward(x)
        right(90)
        spiral(0.9*x) #recursive call
        return

spiral(200)
