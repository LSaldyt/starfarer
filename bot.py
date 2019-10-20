from control import write, press, combo, click
import subprocess, sys

class Bot:
    def __init__(self):
        pass

def main(args):
    combo('ctrl', '`')
    txt = 'echo "This text was written by a bot!"'
    write(txt)
    press('enter')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
