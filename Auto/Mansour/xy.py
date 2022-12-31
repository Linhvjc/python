#! python3
import pyautogui, sys
from threading import Thread
from pynput import keyboard

def exit_program():
    def on_press(key):
        if str(key) == 'Key.esc':
            main.status = 'exit'
            exit()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
def main():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

Thread(target=main).start()
Thread(target=exit_program).start()