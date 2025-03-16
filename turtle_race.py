import turtle
import time

WIDTH, HEIGHT = 500, 500



def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter number of racers(2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input not numeric. Try Again!")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("The number is not in ranger 2-10. Try Again!")


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")
    
racers = get_number_of_racers()
init_turtle()

racer = turtle.Turtle()
racer.speed(2)
racer.penup()
racer.shape('turtle') #turtle, cirle, arrow
racer.color('cyan')
racer.forward(100)
racer.left(90)
racer.pendown()
racer.forward(100)
racer.left(90)
racer.backward(100)
time.sleep(25)

racer_2 = turtle.Turtle()
racer_2.speed(4)
racer_2.penup()
racer_2.shape('turtle') #turtle, cirle, arrow
racer_2.color('green')
racer_2.forward(200)
racer_2.left(90)
racer_2.pendown()
racer_2.forward(200)
racer_2.left(90)
racer_2.backward(200)
time.sleep(25)