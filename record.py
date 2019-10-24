import keyboard  as k
import pyautogui as p

from time import sleep

sample_rate = 0.01
image_directory = 'frames'

def record():
    k.start_recording()
    mouse = []
    i = 0
    while True:
        mouse.append(p.position())
        p.screenshot('frames/{}.png'.format(i))
        sleep(sample_rate)
        if k.is_pressed('f12'):
            break
        i += 1
    keys = k.stop_recording()
    print(mouse)
    print(keys)

record()
