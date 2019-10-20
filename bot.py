from control import write, press, combo, click
from time import sleep
import pyautogui as p
import subprocess, sys

class Bot:
    def __init__(self):
        pass

def main(args):
    combo('alt', '4') # Switch to game screen
    press('space')
    x, y = p.size()
    cx, cy = x // 2, y // 2
    sleep(0.1)
    click(cx, cy, button='right') # Raise shields
    p.keyDown('w')
    while True:
        click(cx, cy - 50, clicks=10)
        sleep(0.1)
    p.keyUp('w')
    press('space')

    #combo('ctrl', '`')
    #txt = 'echo "This text was written by a bot!"'
    #write(txt)
    #press('enter')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
