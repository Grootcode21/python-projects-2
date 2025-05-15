#install curses. pip install windows-curses
import curses
from curses import wrapper
import time
import queue

maze = [

]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            stdscr.addstr(i, j, value)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    #Breadth-search algorithm

    # stdscr.clear()
    # stdscr.addstrs(0, 0, "Hello World!", blue_and_black)
    # stdscr.refresh()
    # stdscr.getch()

wrapper(main)

