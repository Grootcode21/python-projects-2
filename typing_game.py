#pip install curses
#To run: nagivate to where the file is,click at the top C:\Users\ALIENWARE\Desktop\SOURCE CODES\Python Projects 2, type cmd click Enter
import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test")
    stdscr.stdstr("\nPress any key to begin")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_text = "Hello World, this is a nice way to learn typing"
    current_text = []

    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
   
    while True:
        key = stdscr.getkey()
        current_text.append(key)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()



def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.screen(stdscr)
    wpm_test(stdscr)

wrapper(main)