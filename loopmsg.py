import pyautogui
import time
time.sleep(4)
for i in range(150):
    pyautogui.typewrite('number'+ str(i+1) )
    pyautogui.press("enter")
