import pyautogui
import time
time.sleep(4)
for i in range(50):
    pyautogui.typewrite('number'+ str(i) )
    pyautogui.press("enter")
