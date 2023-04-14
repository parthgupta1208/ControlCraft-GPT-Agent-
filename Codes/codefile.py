
import time
import pyautogui
import os

# open whatsapp
os.startfile("C:/Users/USERNAME/AppData/Local/WhatsApp/WhatsApp.exe")
time.sleep(10) # wait for whatsapp to open

# click on search bar
pyautogui.click(60, 153)

# type name of contact
pyautogui.typewrite("Xavier")
time.sleep(2)

# click on contact
pyautogui.click(69, 261)
time.sleep(2)

# click on message box
pyautogui.click(845, 865)

# type message
pyautogui.typewrite("hello")

# press enter to send message
pyautogui.press("enter")
