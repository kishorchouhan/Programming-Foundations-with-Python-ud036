import turtle

def draw_parallelogram(some_turtle):
    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.right(150)
        some_turtle.forward(100)
        some_turtle.right(30)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor('blue')
    #the turtle Brad - draws a parallelogram
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    for i in range(1,37):
        draw_parallelogram(brad)
        brad.right(10)
    brad.right(90)
    brad.forward(200)
        
    window.exitonclick()

draw_flower()
