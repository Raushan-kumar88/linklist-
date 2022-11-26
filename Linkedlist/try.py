import pyautogui
import time
time.sleep(3)
count = 0
while count<=100:
    pyautogui.write("hello how are you"+str(count))
    pyautogui.press("enter")
    count=count+1   
