#install curses. pip install windows-curses
import curses
from curses import wrapper
import time
import queue

maze = [

]


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    #Breadth-search algorithm

    # stdscr.clear()
    # stdscr.addstrs(0, 0, "Hello World!", blue_and_black)
    # stdscr.refresh()
    # stdscr.getch()

wrapper(main)

