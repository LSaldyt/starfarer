import keyboard  as k
import mouse as m
import pyautogui as p

from time import sleep

sample_rate = 0.01
image_directory = 'frames'

def record():
    k.start_recording()
    positions = []
    i = 0
    while True:
        positions.append((m.X, m.X2, m.is_pressed(button='left'), m.is_pressed(button='right'), m.is_pressed(button='middle')))
        p.screenshot('frames/{}.png'.format(i))
        if k.is_pressed('escape'):
            break
        sleep(sample_rate)
        i += 1
    keys = k.stop_recording()
    print(positions)
    print(keys)

record()
