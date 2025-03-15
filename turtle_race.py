import turtle

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
print(racers)

 