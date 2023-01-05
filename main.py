from tkinter import Tk
import keyboard
import translate

translator = translate.Translator('ru')


def trans():
    keyboard.press_and_release('Ctrl+Ins')
    text = Tk().clipboard_get()
    text = translator.translate(text)
    keyboard.send('Right')
    keyboard.write(' (' + text + ')')


keyboard.add_hotkey('F2+F4', trans)
keyboard.add_abbreviation('@@', 'artemiy.zami@gmail.com')
keyboard.wait('esc')
