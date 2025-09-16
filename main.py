import turtle

turtle.speed(10)
def draw_circle():
    for i in range(72):
        turtle.forward(.525*size)
        turtle.right(5)


size = 14
count = 8

def draw_petal():
    for i in range(20):
        turtle.forward(size)
        turtle.right(30/count)
    turtle.right(10*count)
    for i in range(20):
        turtle.forward(size)
        turtle.right(30/count)
    
    turtle.right(26.667*count)

turtle.speed(10)

draw_circle()

turtle.left(180-13.33*count)

for i in range (count+5):
    draw_petal()

turtle.exitonclick()