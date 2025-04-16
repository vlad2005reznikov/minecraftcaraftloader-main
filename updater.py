import wget
import os
import sys
import PySimpleGUI as sg
import webbrowser
import subprocess
import threading
from jabagif import gif
import requests
import importlib.util

username = (os.environ.get("USERNAME"))
folder = 'C:/Users/' + username + '/Documents/abobamine_loader/'
fldir = os.path.abspath(__file__)
auto_url = 'https://pastebin.com/raw/ccByvh5f'
headers = {'User-Agent': 'Mozilla/5.0'}
lo = 0

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
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
    os.remove(resource_path('mod_load_ver.py'))
    os.remove(resource_path('ccByvh5f.py'))
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
        webbrowser.open_new('https://t.me/Vlad_Reznikov')
        window.close()
        os.abort()


def get_url():
    try:
        file_path = resource_path("ccByvh5f.py")
        response = requests.get(auto_url, headers=headers)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
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

module_path = resource_path("ccByvh5f.py")
spec = importlib.util.spec_from_file_location("ccByvh5f", module_path)
ccByvh5f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ccByvh5f)
upd_m_url = ccByvh5f.upd_m_url

newv = upd_m_url + '/mod_load_ver.py'
mine_l = upd_m_url + '/mine_loader.exe'
oldv = upd_m_url + '/oldv.py'
try:
    file_path = resource_path("mod_load_ver.py")
    wget.download(newv, file_path)
except:
    error1()


module_path = resource_path("mod_load_ver.py")
spec = importlib.util.spec_from_file_location("mod_load_ver", module_path)
mod_load_ver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod_load_ver)
v = mod_load_ver.v




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
os.remove(resource_path('mod_load_ver.py'))
os.remove(resource_path('ccByvh5f.py'))
