
import threading
from pynput.mouse import Listener, Button, Controller

clicked = False
def double_click(button):
    global clicked
    mouse = Controller()
    mouse.press(button)
    clicked = False
def on_click(x, y, button, pressed):
    global clicked
    if pressed and not clicked:
        clicked = True
        threading.Thread(target=double_click,args=(button,)).start()
        #a.join()
with Listener(on_click=on_click) as listener:
    listener.join()