import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

#def draw_triangle(some_turtle):
    #some_turtle.right(60)
    #for i in range(1,4):
        #some_turtle.right(120)
        #some_turtle.forward(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    #the turtle Brad - draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    
    #the turtle angie - draws a circle
    #angie = turtle.Turtle()
    #angie.shape('arrow')
    #angie.color('blue')
    #angie.circle(100)
    #the turtle krish - draws a triangle
    #krish = turtle.Turtle()
    #krish.shape('circle')
    #krish.color('green')
    #draw_triangle(krish)
    
    window.exitonclick()

draw_art()
