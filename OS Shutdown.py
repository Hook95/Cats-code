import PySimpleGUI as sg
import os

layout = [[sg.Button('Shut down', font= 'Lucida 14'), sg.Button('Cancel', font= 'Lucida 14', button_color=('white', 'firebrick3'))]]
window = sg.Window('Shutdown', layout)

while True:
    event, values = window.read()
    if event == 'Cancel' or event == sg.WIN_CLOSED:
        break
    else:
        if event == 'Shut down':
            os.system('shutdown -s')
window.close()
