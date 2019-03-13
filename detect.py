from pynput import keyboard as kb
from pynput.keyboard import Key, Controller

from copy import getselectedtext
from combinations import COMBINATIONS
from paste import paste
from window import popup


keyboard = Controller()

# The currently active modifierstr1s
current = set()

ll=['','','','','']
llen=5

def execute():
    if current==COMBINATIONS[0]:
        cot=getselectedtext()
        if cot in ll:
            pass
        elif len(ll)==llen:
            ll.pop()
            ll.insert(0,cot)
            print(cot)
        else:
            ll.append(cot)
            print(cot)

    elif current==COMBINATIONS[1]:
        print(ll)
        popup(ll)
        # paste(ll)
        # paste(xx)

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            # This fun exexuted when th combination i s pressed
            # print(current)
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with kb.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
