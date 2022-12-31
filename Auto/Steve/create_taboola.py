
import pyautogui, sys
import time

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
def ctrl_shift_k():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.keyDown('k')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('k')
def right_click(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.click(button='left')
    
times = 6

# create (times) tab
alt_tab()
for i in range(0,times):
    ctrl_shift_k()

for i in range(1, times+1):
    # link
    right_click(76,16)
    ctrl_c()
    for j in range(0, i):
        ctrl_tab()
    time.sleep(0.3)
    right_click(692,391)
    ctrl_v()
    
    # title 2
    right_click(76,16)
    for j in range(0,10):
        pyautogui.press('left')
    ctrl_c()
    for j in range(0, i):
        ctrl_tab()
    time.sleep(0.3)
    right_click(776,661)
    ctrl_v()
    
    # title 1
    right_click(76,16)
    pyautogui.press('left')
    ctrl_c()
    for j in range(0, i):
        ctrl_tab()
    time.sleep(0.3)
    right_click(776,538)
    ctrl_v()
    pyautogui.scroll(-1000)
    
    # next to another
    right_click(76,16)
    pyautogui.press('down')
    for j in range(0,11):
        pyautogui.press('right')
    
    
    
    
    
    
    



