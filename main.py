import serial
import time
import pyautogui
import re

ser = serial.Serial("COM6", 9600)
time.sleep(1)

print("Forward to start, Backward to end.")

while 1:

    start = str(ser.readline())
    start = re.sub(r'^b\'(.*)\\r\\n\'$', r'\1', start)

    if start == "Forward":
        print(start, " Execution is started.")

    while start == "Forward":

        incoming = str(ser.readline())
        incoming = re.sub(r'^b\'(.*)\\r\\n\'$', r'\1', incoming)
        print(incoming)

        if incoming == 'Left':
            pyautogui.press('left')
        if incoming == 'Right':
            pyautogui.press('right')
        if incoming == 'Clockwise':
            pyautogui.press('volumeup')
        if incoming == 'anti-clockwise':
            pyautogui.press('volumedown')
        if incoming == 'Up':
            pyautogui.press('playpause')
        if incoming == 'Down':
            pyautogui.press('volumemute')
        if 'Backward' in incoming:
            print("Excution stopped")
            break

        incoming = ""

ser.close()