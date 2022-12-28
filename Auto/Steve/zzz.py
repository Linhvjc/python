import pyautogui
import time
import random
first = 1
count = 0
ran =["go", "vuot kho", "len nao", "toi se thang", "hay tin toi", "get go"]

def nhay_tab():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('tab')

def copy_anh():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('c')

def paste_anh():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')

def nhay_window():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('tab')

def cmt(param):
    a = random.randint(1,5)
    comments = f'#TigerArena #DauTruongBanLinh {ran[a]} {param}'
    
    time.sleep(1)
    pyautogui.typewrite(comments)
    time.sleep(1.5)
    pyautogui.press('enter')

def enter():
    pyautogui.typewrite("\n")

while (True):
    if first ==1: 
        time.sleep(5)
        first +=1
    nhay_tab()
    copy_anh()
    nhay_tab()
    cmt('@')
    time.sleep(1.5)
    paste_anh()
    time.sleep(1)
    nhay_window()
    time.sleep(1)
    nhay_tab()
    time.sleep(1)
    copy_anh()
    time.sleep(1)
    nhay_tab()
    time.sleep(1)
    cmt('@')
    time.sleep(1)
    paste_anh()
    time.sleep(8)
    nhay_window()
    time.sleep(1)
    enter()
    time.sleep(1)
    nhay_window()
    time.sleep(2)
    enter()
    time.sleep(1)
    nhay_window()
    time.sleep(1)
    count +=1
    print(count)
    # if count %20 == 0:
    #     time.sleep(120)
    #     pyautogui.keyDown('ctrl')
    #     pyautogui.keyDown('tab')
    #     pyautogui.keyUp('ctrl')
    #     pyautogui.keyUp('tab') 
    #     pyautogui.typewrite('Đa cmt đc 50')
    #     pyautogui.press('enter')
    #     time.sleep(2)
    #     pyautogui.keyDown('ctrl')
    #     pyautogui.keyDown('tab')
    #     pyautogui.keyUp('ctrl')
    #     pyautogui.keyUp('tab')
    #     time.sleep(300)