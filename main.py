import turtle

turtle.speed(0)
def draw_circle():
    for i in range(72):
        turtle.forward(.525*size)
        turtle.right(5)


size = 10 # Can put any value for size of petal

count = 6 # Change to control amount of petals (only 6 and 8 are working rn)

initial_angle = 180-13.33*count # b  FIX THIS

sector_angle = 360 / count # a

theta = (sector_angle + initial_angle)/40


overshoot = 20*theta - initial_angle - sector_angle/2 # ov

tip_angle = 180-2*overshoot



def draw_petal():
    for i in range(20):
        turtle.forward(size)
        turtle.right(theta)
    turtle.left(tip_angle)
    for i in range(20):
        turtle.forward(size)
        turtle.right(theta)
    
    turtle.right(26.667*count)

turtle.speed(20)

draw_circle()

turtle.left(initial_angle)

for i in range (count):
    draw_petal()

turtle.hideturtle

turtle.exitonclick()