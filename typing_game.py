#pip install curses
#To run: nagivate to where the file is,click at the top C:\Users\ALIENWARE\Desktop\SOURCE CODES\Python Projects 2, type cmd click Enter
import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.clear()
    #stdscr.addstr("Hello World", curses.color_pair(2))
    stdscr.addstr(1,0, "Hello World")
    stdscr.refresh()
    key = stdscr.getkey()
    print(key)

wrapper(main)