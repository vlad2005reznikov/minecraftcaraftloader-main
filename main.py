import PySimpleGUI as sg
import wget
import os, shutil
import zipfile
import threading
import sys
import requests

url = 'http://s589698.ha003.t.justns.ru/upd/archiv/ser_mods.zip'
username = (os.environ.get("USERNAME"))
folder = 'C:/Users/' + username + '/AppData/Roaming/.minecraft/mods/'
BAR_MAX = 100
prp = 0
oldfolder = '...'
documents = 'C:/Users/' + username + '/Documents/abobamine_loader/'
admpass: str = '22848'
archive_name = "ser_mods.zip"

sys.path.insert(1, documents)
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

def newconf():
    try:
        os.remove(documents+'config.py')
    except:
        pass
    createfile = open(documents+"config.py","w+", encoding='UTF-8')
    createfile.write("oldfolder = '"+folder+"'")
    createfile.close()

def adminupload():
    try:
        os.remove(folder + 'ser_mods.zip')
    except:
        pass
    window['admuploadtext'].update('Загрузка, ожидайте', visible=True)
    archive_path = os.path.join(folder, archive_name)

    # Создаем архив
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder)
                zipf.write(file_path, arcname=arcname)

    print(f"Архив {archive_name} успешно создан в папке {folder}.")

    with open(folder + 'ser_mods.zip', 'rb') as file:
        # Отправляем файл на сервер
        response = requests.post('http://185.188.183.213/index.php',
                                 files={'file': file})

    # Проверяем успешность запроса
    if response.status_code == 200:
        window['admuploadtext'].update('Файл загружен', visible=True)
    else:
        window['admuploadtext'].update('Ошибка загрузки', visible=True)
    try:
        os.remove(folder + 'ser_mods.zip')
    except:
        pass
try:
    from config import oldfolder
    folder = oldfolder
except:
    pass

# Define the window's contents
layout1 = [[sg.Text("Mod loader", size=(40, 1))],
          [sg.Text(size=(40, 1), visible=False, key='-OUTPUT-')],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20, 20), visible=False, key='pp')],
          [sg.Text(size=(40, 1), visible=False, key='procent')],
           [sg.Button('Загрузить'), sg.Button('Настройки'), sg.Button('Выйти')],
          [sg.Column(
              [[sg.Text("developed by AbobaCorp", font='Default 7', justification='right'), sg.Image("abcorp.png")]],
              justification='right', element_justification='right')]]
layout2 =[
            [sg.Text("Выберите папку установки майнкрафта")],
            [sg.InputText([oldfolder], disabled=True, size=(50,1), key='-FILESLB-'),
            sg.Input(visible=False, enable_events=True, key='custompth'), sg.FolderBrowse('Обзор')],
            [sg.Button('Назад'), sg.Button('Админ меню'), sg.Button('Сбросить')]
]

layout3 =[[sg.Text("Админ меню")],
    [sg.Text("Введите пароль"),sg.InputText(key='adminpassbyuserwindow'), ],
    [sg.Text('Пароль не верный',key='pass incorrect' ,visible=False)],
    [sg.Button("Назад", key='back adm'), sg.Button("Ок", key='pass confirmation')]
]

layout4 =[[sg.Text("Админ меню")],
[sg.Text("Обновление файлов",size=(40, 1))],
[sg.Text(key='admuploadtext',visible=False)],
[sg.Button("Назад", key='backadm2'), sg.Button("Обновить файлы", key='updfile server')]
]

layout = [[sg.Column(layout1, key='main'), sg.Column(layout2, visible=False, key='setings'), sg.Column(layout3, visible=False, key='admin'),
           sg.Column(layout4, visible=False, key='authadmin')]
          ]
window = sg.Window('ServerName mod loader', layout, icon='logo.ico')

while True:
    event, values = window.read(timeout=10)
    # See if user wants to quit or window was closed
    if event == 'custompth':
        window['-FILESLB-'].Update(values['custompth'])
        folder = values['custompth']+'/mods'
        newconf()
    if event == 'Сбросить':
        try:
            os.remove(documents+'config.py')
            folder = 'C:/Users/' + username + '/AppData/Roaming/.minecraft/mods/'
            window['-FILESLB-'].update('...')
        except:
            pass
    if event == 'Настройки':
        window['main'].update(visible=False)
        window['setings'].update(visible=True)
    if event == 'Назад':
        window['setings'].update(visible=False)
        window['main'].update(visible=True)
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
    if event == 'Админ меню':
        window['setings'].update(visible=False)
        window['admin'].update(visible=True)
    if event == 'back adm':
        window['admin'].update(visible=False)
        window['setings'].update(visible=True)
    if event == 'pass confirmation':
        adminpassbyuser: str = values['adminpassbyuserwindow']
        if adminpassbyuser == admpass:
            window['admin'].update(visible=False)
            window['authadmin'].update(visible=True)
        else:
            window['pass incorrect'].update(visible=True)
    if event == 'backadm2':
        window['authadmin'].update(visible=False)
        window['admin'].update(visible=True)
    if event == 'updfile server':
        th = threading.Thread(target=adminupload)
        th.start()

# Finish up by removing from the screen

window.close()
