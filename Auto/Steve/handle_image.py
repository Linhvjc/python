import pyautogui, sys
import time
import random

dict_temp = "D:\Job\Steve\\temp"

# #! Attorneys
# dict = 'D:\Job\Steve\Images\Attorneys\CN'
# name = '"P004" "P001" "P002" "P003" '

# #! Credit cards
# dict = 'D:\Job\Steve\Images\Credit Cards\CA'
# name = '"P001" "P002" "P003" "P004" "P005" "P006" '

# #! Digital Marketing Courses
# dict = 'D:\Job\Steve\Images\Digital Marketing Courses\ES'
# name = '"P001" "P002" "P003" "P004" "P005" "P006" "P007" "P008" "P009" "P010" '

# #! Drug Rehab
# dict = 'D:\Job\Steve\Images\Drug Rehab\General'
# name = '"P001" "P002" "P003" "P004" "P005" "P006" "P007" "P008" '

# #! Funeral Services
# dict = 'D:\Job\Steve\Images\Funeral Services\General'
# name = '"P001" "P002" "P003" "P004" "P005" "P006" "P007" "P008" "P009" '

#! Laser liposuction
dict = "D:\Job\Steve\Images\Laser Liposuction\General"
name = '     "P001" "P002" "P003" "P004" "P005" "P006"         '

# #! Personal Loans
# dict = 'D:\Job\Steve\Images\Personal Loans\MY'
# name = '"P001" "P002" "P003" "P004" "P005" "P006"  '

# dict = 'D:\Job\Steve\Images\Personal Loans\TH'
# name = '"P001" "P002" "P003" "P004" "P005" "P006" '

image_name = name.strip()
image_name = image_name[1:-1]
image_name = image_name.split('" "')


try:
    x, y = pyautogui.position()
        
    time.sleep(3)
    for i in range(0, len(image_name)):
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
        
        # Save 
        pyautogui.moveTo(1340, 794)
        pyautogui.click(button='left')
        pyautogui.press('enter')
        time.sleep(0.5)
    
    # Show option
    # pyautogui.keyDown('shift')
    # pyautogui.keyDown('fn')
    # pyautogui.keyDown('f10')
    # pyautogui.keyUp('shift')
    # pyautogui.keyUp('fn')
    # pyautogui.keyUp('f10')
    
    # Move mouse and right click
    # pyautogui.moveTo(277, 250)
    # pyautogui.click(button='right')
    
except KeyboardInterrupt:
    print('\n')