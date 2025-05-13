#install curses. pip install windows-curses
import curses
from curses import wrapper
import time
import queue

maze = [

]


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    blue_and_black = curses.color_pair(1)

    stdscr.clear()
    stdscr.addstrs(0, 0, "Hello World!", blue_and_black)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)

