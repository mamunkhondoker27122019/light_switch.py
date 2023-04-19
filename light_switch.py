import keyboard
import time

light_on = False

while True:
    if keyboard.is_pressed('space'):
        light_on = not light_on
        if light_on:
            print("Свет включен.")
        else:
            print("Свет выключен.")
        time.sleep(0.2)
