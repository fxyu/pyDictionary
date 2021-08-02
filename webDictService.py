# 引入套件
import clipboard
from pynput.keyboard import Key, Listener, Controller

import urllib3
import time

import config
# from ctypes import windll

# ================================
# Input Listener
# ================================
key_pressed = set()
obj = {}
keyboardCtrl = Controller()
url = config.SERVER_URL

http = urllib3.PoolManager()
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
headers = { 'User-Agent' : user_agent }

# window = tk.Tk()

def on_press(key):

    try:
        if Key.alt_l in key_pressed:
            if hasattr(key,'char'):
                if key.char == "c":
                    keyboardCtrl.release(Key.alt_l.value) #this would be for your key combination
                    keyboardCtrl.release("c")

                    keyboardCtrl.press(Key.ctrl_l.value) #this would be for your key combination
                    keyboardCtrl.press("c")
                    keyboardCtrl.release("c")
                    keyboardCtrl.release(Key.ctrl_l.value) #this would be for your key combination
                    
                    time.sleep(.05)
                    while True:
                        try:
                            cb = clipboard.paste()
                            break
                        except:
                            pass
                    word_search(cb)

        key_pressed.add(key)
        # print(f'{key} pressed.')
    except Exception as e:
        print(e)

def on_release(key):
    key_pressed.discard(key)
    # print(f'{key} released.')

    # if key == Key.esc:
    #     return False

def word_search(word):
    print(word)
    search_url = "{}search/{}".format(url, word)
    http.request('GET',search_url,headers=headers)


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

