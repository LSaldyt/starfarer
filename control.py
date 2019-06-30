#!/usr/bin/env python3
import sys
import pyautogui as p
from time import sleep

from contextlib import contextmanager

p.FAILSAFE = False

@contextmanager
def key_held(*args, **kwargs):
    p.keyDown(*args, **kwargs)
    yield
    p.keyUp(*args, **kwargs)

def combo(modifier, key):
    with key_held(modifier):
        p.press(key)

write = p.typewrite
click = p.click
press = p.press

def main(args):
    combo('ctrl', '`')
    txt = 'echo "This text was written by a bot!"'
    write(txt)
    press('enter')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
