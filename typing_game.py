#pip install curses
import curses
from curses import wrapper

def main(stdscr):
    stdscr.addstr("Hello World")

wrapper(main)