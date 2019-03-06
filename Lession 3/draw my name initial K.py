import turtle

def draw_K():
    window = turtle.Screen()
    window.bgcolor('red')
    #the turtle Brad - draws a square
    K = turtle.Turtle()
    K.shape("turtle")
    K.color("green")
    K.speed(2)
    K.right(90)
    K.forward(100)
    K.right(180)
    K.forward(50)
    K.right(45)
    K.forward(70)
    K.right(180)
    K.forward(65)
    K.left(90)
    K.forward(70)

    window.exitonclick()

draw_K()
