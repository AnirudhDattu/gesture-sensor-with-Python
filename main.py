import serial
import time
import pyautogui
import re
import serial.tools.list_ports

# Function to find the COM port based on device name
def find_device_port(device_name):
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if device_name in port.description:     
            return port.device
    return None

# Specify your device name
device_name = "Arduino Uno"

# Find the COM port dynamically

com_port = find_device_port(device_name)

if com_port is None:
    print(f"Device '{device_name}' not found. Check the connection.")
else:
    ser = serial.Serial(com_port, 9600)
    time.sleep(1)

    print("Forward to start, Backward to end.")

    while True:
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
                print("Execution stopped")
                break

            incoming = ""

    ser.close()
