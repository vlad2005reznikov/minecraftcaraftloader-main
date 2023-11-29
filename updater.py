import wget
import os
import shutil
import sys
import PySimpleGUI as sg
import webbrowser
import subprocess

username = (os.environ.get("USERNAME"))
folder = 'C:/Users/' + username + '/Documents/abobamine_loader/'
fldir = os.path.abspath(__file__)
auto_url = 'https://pastebin.com/raw/ccByvh5f'


def update_mine():
    try:
        os.remove(folder + 'mine_loader.exe')
        os.remove(folder + 'oldv.py')
    except:
        pass
    wget.download(mine_l, folder + 'mine_loader.exe')
    wget.download(oldv, folder + 'oldv.py')
    os.system(folder + 'mine_loader.exe')
    sys.path.insert(1, fldir)
    os.remove('mod_load_ver.py')
    os.abort()


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
