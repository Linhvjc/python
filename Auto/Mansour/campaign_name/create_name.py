import pyautogui, sys
import time

times =8

def ctrl_c():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('c')

def ctrl_v():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')
    
def ctrl_z():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('z')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('z')
    
def alt_tab():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('tab')
def ctrl_tab():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('tab')
    
time.sleep(1)

for i in range(0,times):
    # Switch tab
    alt_tab()

    # Copy text
    ctrl_c()
    # switch tab
    alt_tab()
    # paste text
    pyautogui.moveTo(685,193)
    pyautogui.click(button='left')
    ctrl_v()
    # switch tab
    alt_tab()
    
    # Get device
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    ctrl_c()
    alt_tab()
    pyautogui.moveTo(753, 340)
    pyautogui.click(button='left')
    ctrl_v()
    alt_tab()
    
    # Get title
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    ctrl_c()
    alt_tab()
    #paste title
    pyautogui.moveTo(701, 400)
    pyautogui.click(button='left')
    ctrl_v()
    alt_tab()
    
    #get date
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    ctrl_c()
    # switch tab
    alt_tab()
    #paste date
    pyautogui.moveTo(701,460)
    pyautogui.click(button='left')
    ctrl_v()
    # run
    pyautogui.keyDown('shift')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('enter')
    #reset
    pyautogui.scroll(1000)
    pyautogui.moveTo(1297, 385)
    pyautogui.click(button='left')
    ctrl_z()
    ctrl_z()
    ctrl_z()
    ctrl_z()
    pyautogui.scroll(1000)


    # Copy result
    pyautogui.moveTo(662,695)
    time.sleep(0.5)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    time.sleep(0.5)
    ctrl_c()
    ctrl_c()

    #Switch tab and paste
    alt_tab()
    for i in range(0,14):
        pyautogui.press('right')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')
    
    # remove ''
    pyautogui.press('enter')
    pyautogui.press('backspace')
    for i in range(0,15):
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('left')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('left')
    pyautogui.press('delete')
    pyautogui.press('enter')

    #next line
    pyautogui.press('left')
    pyautogui.press('left')
    alt_tab()