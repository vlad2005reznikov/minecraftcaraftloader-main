import wget
import os
import sys
import PySimpleGUI as sg
import webbrowser
import subprocess
import threading
from jabagif import gif

username = (os.environ.get("USERNAME"))
folder = 'C:/Users/' + username + '/Documents/abobamine_loader/'
fldir = os.path.abspath(__file__)
auto_url = 'https://pastebin.com/raw/ccByvh5f'
lo = 0

def update_mine():
    try:
        os.remove(folder + 'mine_loader.exe')
        os.remove(folder + 'oldv.py')
    except:
        pass
    th = threading.Thread(target=logif)
    th.start()
    wget.download(mine_l, folder + 'mine_loader.exe')
    wget.download(oldv, folder + 'oldv.py')
    global lo
    lo = 1
    subprocess.call(folder + 'mine_loader.exe')
    sys.path.insert(1, fldir)
    os.remove('mod_load_ver.py')
    os.remove('ccByvh5f.py')
    os.abort()


def logif():
    sg.theme('SystemDefault1')
    layout = [[sg.Text('Обновление, пожалуйста подождите')],
              [sg.Image(data=gif, key='-IMAGE-')],
              [sg.Button('Выход')]]
    window1 = sg.Window('Обновление компонентов', layout)
    while lo < 1:  # Event Loop
        event, values = window1.read(timeout=10)  # loop every 10 ms to show that the 100 ms value below is used for animation
        if event in (sg.WIN_CLOSED, 'Выход'):
            window1.close()
            os.abort()
        window1['-IMAGE-'].update_animation(gif, time_between_frames=30)

def error1():
    sg.theme('SystemDefault1')
    layout = [[sg.Text('Сервер обновления не отвечает')],
              [sg.Text('Пните Влада, чтобы сервак включил')],
              [sg.Button('Ok'), sg.Button('Пнуть')]]
    window = sg.Window('Ошибка', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            window.close()
            os.abort()
        webbrowser.open_new('https://vk.com/v.reznikov2005')
        window.close()
        os.abort()


def get_url():
    try:
        wget.download(auto_url, 'ccByvh5f.py')
    except:
        error1()


try:
    os.remove('ccByvh5f.py')
except:
    pass
try:
    os.remove('mod_load_ver.py')
except:
    pass
get_url()
from ccByvh5f import upd_m_url

newv = upd_m_url + '/mod_load_ver.py'
mine_l = upd_m_url + '/mine_loader.exe'
oldv = upd_m_url + '/oldv.py'
try:
    wget.download(newv, 'mod_load_ver.py')
except:
    error1()
from mod_load_ver import v

try:
    os.makedirs(folder)
    update_mine()
except:
    pass
try:
    sys.path.insert(1, folder)
    from oldv import vold
except:
    update_mine()
if v > vold:
    update_mine()
else:
    pass

subprocess.call(folder + 'mine_loader.exe')
sys.path.insert(1, fldir)
os.remove('mod_load_ver.py')
os.remove('ccByvh5f.py')
