
import os
import pyautogui
import random

# Open MS-Excel
os.startfile("excel.exe")

# Wait for Excel to open and Maximize the window
pyautogui.sleep(5)
pyautogui.hotkey('win', 'up')

# Create list of random names
names = []
for i in range(60):
    random_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=7))
    names.append(random_name)

# Click on first cell and start entering names
pyautogui.click(x=110, y=216)
for name in names:
    pyautogui.typewrite(name)
    pyautogui.press('enter')
