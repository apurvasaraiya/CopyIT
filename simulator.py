from pynput.keyboard import Key, Controller
import time

def paste(*str1):
    keyboard = Controller()
    print(str1[0])

    for i in str1[0]:
        # time.sleep(0.1)
        print(i)
        if i=='\n' or i=='\r':
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif i=='\t':
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
        else:
            keyboard.press(i)
            keyboard.release(i)
