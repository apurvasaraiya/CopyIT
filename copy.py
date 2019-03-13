import os

def getselectedtext():
    current_text=""
    while True:
        cot=os.popen('xsel').read()
        if current_text!=cot:
            current_text=cot
            return cot
