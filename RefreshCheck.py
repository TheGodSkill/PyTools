import PySimpleGUI as sg
import win32api

# Get the monitor's refresh rate
refresh_rate = round(win32api.EnumDisplaySettings(None, 0).DisplayFrequency)

# Create the GUI
layout = [[sg.Text(f"Your monitor's refresh rate is {refresh_rate} Hz")],
          [sg.Button('Output')]]

window = sg.Window('Monitor Refresh Rate Checker', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Output':
        with open('refresh_rate.txt', 'w') as f:
            f.write(str(refresh_rate))

window.close()
