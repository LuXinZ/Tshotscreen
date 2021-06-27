# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import io
import sys
from PIL import ImageGrab
import pyautogui as pag
import pynput
from pynput import keyboard
import pytesseract
import time
from PIL import Image
import requests
from urllib.parse import urlencode
from spider import go_request
Msx = 0
Msy = 0
Mox = 0
Moy = 0


def init():
    with keyboard.Listener(
            on_press=on_press,
    ) as listener:
        listener.join()


def on_press(key):
    global MSx
    global MSy
    global Mox
    global Moy
    try:
        if key.char == "2":
            X, Y = pag.position()
            Mox = X
            Moy = Y
            draw()
            return False
        if key.char == "1":
            MouseX, MouseY = pag.position()
            MSx = MouseX
            MSy = MouseY

    except AttributeError:
        print('special key {0} pressed'.format(key))


# Press the green button in the gutter to run the script.
def draw():
    global Msx
    global Msy
    global Mox
    global Moy

    im = ImageGrab.grab(bbox=(MSx * 2, MSy * 2, Mox * 2, Moy * 2))
    im.save('./png/1.png')
    f = open('./png/1.png', 'rb')
    pil_img = Image.open(io.BytesIO(f.read()))

    result = pytesseract.image_to_string(
        pil_img, timeout=5, lang=(sys.argv[1] if len(sys.argv) > 1 else None)
    ).strip()
    text = urlencode({
        'text': 'nihao',
        'from': 'en',
        'to': 'zh-cn',
    })
    print(text)
    res = requests.get('http://localhost:30031/?')
    print(res)
    # print(requests.get('http://localhost:30031/?' + urlencode({
    #     'text': 'I spea Dutch!',  # this input will trigger auto-suggestion
    #     'from': 'en',  # leave blank to auto detect
    #     'to': 'zh-cn',
    #     # 'raw': 'true',  # response contains unparsed response
    #     # 'domain': 'cn'  # change google translate domain, overrides default domain
    # })).json())
    # time.sleep(1)


if __name__ == '__main__':
    #init()
    go_request()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
