"""

This is a scrip that creates a fractal, specifically the Sierpinsky triangle, using the iterative algorithm made with processing.

Author 
Saúl López

"""

#Constant
HEIGHT = 700
WEIGHT = 500 

#variables
v1 = PVector(10,450)
v2 = PVector(690,450)
v3 = PVector(HEIGHT/2,50)
seedPoint= PVector(HEIGHT/2, 150)
vertex = PVector(0,0)
r = []
pm= MiddlePoint(0,0)

def setup():
    size(HEIGHT,WEIGHT)
    background(51)

def draw():

    vertex.x=0
    vertex.y =0
    
    #triangle
    stroke(255)
    line(v1.x,v1.y,v3.x,v3.y)
    line(v2.x,v2.y,v3.x,v3.y)
    line(v1.x,v1.y,v2.x,v2.y)
    
    rng = random(0,1)

    if (rng < (.333333333)):
        vertex.x = v1.x
        vertex.y = v1.y
    elif (rng < (.66666)):
        vertex.x = v2.x
        vertex.y = v2.y
    elif (rng >(.66666)):
        vertex.x = v3.x
        vertex.y = v3.y
    
    if ( frameCount == 1):
        pm.x = (vertex.x+seedPoint.x)/2
        pm.y = (vertex.y+seedPoint.y)/2
    else:
        pm.x = (vertex.x+pm.x)/2
        pm.y = (vertex.y+pm.y)/2

    point(pm.x,pm.y)
    point(seedPoint.x,seedPoint.y)
    
