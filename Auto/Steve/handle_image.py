import pyautogui, sys
import time
import random
from threading import Thread
from pynput import keyboard

def exit_program():
    def on_press(key):
        if str(key) == 'Key.esc':
            main.status = 'exit'
            exit()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

dict_temp = "D:\Job\Steve\\temp\pe5"

# #! Attorneys
# dict = 'D:\Job\Steve\Images\Attorneys\CN'
# name = '"P004" "P001" "P002" "P003" '

# #! Credit cards
# dict = 'D:\Job\Steve\Images\Credit Cards\CA'
# name = '"P001" "P002" "P003" "P004" "P005" "P006" '

# # #! Dental Implants
# dict = 'D:\Job\Steve\Images\Dental Implants\Asia'
# name = '"P001" "P002" "P003" "P004" "P005" "P006" "P007" "P008" "P009" "P010" '

# # #! Cell phones
# dict = 'D:\Job\Steve\Images\Cell phones\General'
# name = '"P001" "P002" "P003" "P004" "P005" "P006" "P007" '



# #! Digital Marketing Courses
# dict = 'D:\Job\Steve\Images\Digital Marketing Courses\Asia'
# name = '"P010" "P001" "P002" "P003" "P004" "P005" "P006" "P007" "P008" "P009"  '

# #! Drug Rehab
# dict = 'D:\Job\Steve\Images\Drug Rehab\General'
# name = '"P001" "P002" "P003" "P004" "P005" "P006" "P007" "P008" '

# #! Funeral Services
# dict = 'D:\Job\Steve\Images\Funeral Services\General'
# name = '"P001" "P002" "P003" "P004" "P005" "P006" "P007" "P008" "P009" '

# #! Laser liposuction
# dict = "D:\Job\Steve\Images\Laser Liposuction\General"
# name = '     "P001" "P002" "P003" "P004" "P005" "P006"         '

#! Personal Loans
dict = 'D:\Job\Steve\Images\Personal Loans\EU'
name = '"P001" "P002" "P003" "P004" "P005" "P006" "P007" "P008" "P009" "P010"  '

# dict = 'D:\Job\Steve\Images\Personal Loans\TH'
# name = '"P001" "P002" "P003" "P004" "P005" "P006" '

image_name = name.strip()
image_name = image_name[1:-1]
image_name = image_name.split('" "')

def main():
    try:
        x, y = pyautogui.position()
        time.sleep(3)
        
        for i in range(0, len(image_name)):
            main.status = 'run' 
            # check key interrupt
            if main.status == 'exit':
                print('Main program closing')
                break
            # Open
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('o')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('o')
            time.sleep(0.5)
            
            # move and enter dict
            pyautogui.moveTo(781, 308)
            pyautogui.click(button='left')
            pyautogui.typewrite(dict)
            pyautogui.press('enter')
            
            # Move and enter image name
            pyautogui.moveTo(959, 750)
            pyautogui.click(button='left')
            pyautogui.typewrite(image_name[i])
            pyautogui.press('enter')
            
            # check key interrupt
            if main.status == 'exit':
                print('Main program closing')
                break
            # choose pencil
            pyautogui.moveTo(360, 129)
            pyautogui.click(button='left')
            
            # choose weight line
            pyautogui.moveTo(959, 155)
            pyautogui.click(button='left')
            pyautogui.moveTo(959, 218)
            pyautogui.click(button='left')
            pyautogui.click(button='left')
            
            # Draw 3 dots
            for i in range(0,3):
                x1 = random.randint(80,530)
                y1 = random.randint(350,600)
                pyautogui.moveTo(x1, y1)
                pyautogui.click(button='left')
                time.sleep(0.2)
            
            # click Save as
            pyautogui.moveTo(30, 64)
            pyautogui.click(button='left')
            pyautogui.moveTo(313, 267)
            pyautogui.click(button='left')
            time.sleep(0.7)
            pyautogui.moveTo(400, 310)
            pyautogui.click(button='left')
            pyautogui.click(button='left')
            time.sleep(0.5)
            
            # Open temp folder
            pyautogui.moveTo(779, 309)
            pyautogui.click(button='left')
            pyautogui.typewrite(dict_temp)
            pyautogui.press('enter')
            time.sleep(0.5)
            # check key interrupt
            if main.status == 'exit':
                print('Main program closing')
                break
                
            # Save 
            pyautogui.moveTo(1340, 794)
            pyautogui.click(button='left')
            pyautogui.press('enter')
            time.sleep(0.5)
        main.status = 'exit'
        exit()
    except KeyboardInterrupt:
        print('\n')

Thread(target=main).start()
Thread(target=exit_program).start()