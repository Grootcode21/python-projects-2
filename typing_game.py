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

def display_text(stdscr, target, current, wpm=0):
        stdscr.addstr(target) 

        for i, char in enumerate(current):
            correct_char = target[i]
            stdscr.addstr(0,i, char, curses.color_pair(1))

def wpm_test(stdscr):
    target_text = "Hello World, this is a nice way to learn typing"
    current_text = []


   
    while True:
        stdscr.clear()
        display_text(stdscr, target_text,  current_text)


        stdscr.refresh()

        key = stdscr.getkey()

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)





def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.screen(stdscr)
    wpm_test(stdscr)

wrapper(main)