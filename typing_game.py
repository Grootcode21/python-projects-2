#pip install curses
#To run: nagivate to where the file is,click at the top C:\Users\ALIENWARE\Desktop\SOURCE CODES\Python Projects 2, type cmd click Enter
import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello World")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)