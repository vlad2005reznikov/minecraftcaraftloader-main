import PySimpleGUI as sg
import wget
import os, shutil
import zipfile
import threading

url = 'http://s589698.ha003.t.justns.ru/upd/archiv/ser_mods.zip'
username = (os.environ.get("USERNAME"))
folder = 'C:/Users/' + username + '/AppData/Roaming/.minecraft/mods/'
BAR_MAX = 100
prp = 0


# sg.theme('black')
def download():
    try:
        shutil.rmtree(folder)
    except:
        pass
    os.makedirs(folder)
    wget.download(url, folder + 'ser_mods.zip', bar=bar_custom)
    z = zipfile.ZipFile(folder + 'ser_mods.zip', 'r')
    z.extractall(folder)
    z.close()
    os.remove(folder + 'ser_mods.zip')
    window['-OUTPUT-'].update("Загрузка завершена.")


def bar_custom(current, total, width=80):
    window["pp"].update(visible=True)
    window["procent"].update(visible=True)
    prp = current / total * 100
    window['pp'].update(prp)
    percentage = (f'{int(prp)}%')
    window['procent'].update(percentage)


# Define the window's contents
layout = [[sg.Text("Mod loader", size=(40, 1))],
          [sg.Text(size=(40, 1), visible=False, key='-OUTPUT-')],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20, 20), visible=False, key='pp')],
          [sg.Text(size=(40, 1), visible=False, key='procent')],
          [sg.Button('Загрузить'), sg.Button('Выйти')],
          [sg.Column(
              [[sg.Text("developed by AbobaCorp", font='Default 7', justification='right'), sg.Image("abcorp.png")]],
              justification='right', element_justification='right')]]

# Create the window
window = sg.Window('ServerName mod loader', layout, icon='logo.ico')

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read(timeout=10)
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Выйти':
        break
    # Output a message to the window
    if event == 'Загрузить':
        window['-OUTPUT-'].update(visible=True)
        window['-OUTPUT-'].update("Загрузка, подождите...")
        try:
            th = threading.Thread(target=download)
            th.start()
        except:
            window['-OUTPUT-'].update("Чёт пошло не так")

# Finish up by removing from the screen

window.close()
