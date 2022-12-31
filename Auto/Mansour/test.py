import time
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
    main.status = 'run'

    while True:
        print('running')
        time.sleep(1)

        while main.status == 'pause':
            time.sleep(1)

        if main.status == 'exit':
            print('Main program closing')
            break


Thread(target=main).start()
Thread(target=exit_program).start()