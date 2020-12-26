import tkinter
from tkinter import *
import winsound
import time




def Clean_stroke(content):
    result = []
    content = str(content).lower()

    for element in content:
        if (ord(element) >= 1072 and ord(element) <= 1103 ):
            result.append(element)
        elif ord(element)==32:
            result.append(' ')

    return result


def Russian_to_Morse(content):


    content = Clean_stroke(content)
    result = []

    for element in content:
        result.append(rus_to_morse[element])

    for set in result:
        for symbol in set:
            if symbol == '.':
                winsound.Beep(frequency, 100)
            elif symbol == '-':
                winsound.Beep(frequency, 400)
    b=' '.join(result)
    return b

def morse():
    return strv.set(Russian_to_Morse(strv.get()))

def MTR1():
    return strv.set(MTR(strv.get()))
def MTR(c1):
    с1=strv.get()
    CODE_REVERSED = {value:key for key,value in rus_to_morse.items()}
    b1=''.join(CODE_REVERSED.get(i) for i in с1.split(' '))
    return b1

def tochka(event):
    winsound.Beep(frequency, 40)
def tire(event):
    winsound.Beep(frequency,100)

rus_to_morse = {'а': '.-',
                    'б': '-...',
                    'в': '.--',
                    'г': '--.',
                    'д': '-..',
                    'е': '.',
                    'ж': '...-',
                    'з': '--..',
                    'и': '..',
                    'й': '.---',
                    'к': '-.-',
                    'л': '.-..',
                    'м': '--',
                    'н': '-.',
                    'о': '---',
                    'п': '.--.',
                    'р': '.-.',
                    'с': '...',
                    'т': '-',
                    'у': '..-',
                    'ф': '..-.',
                    'х': '....',
                    'ц': '-.-.',
                    'ч': '---.',
                    'ш': '----',
                    'щ': '--.-',
                    'ъ': '.--.-.',
                    'ы': '-.--',
                    'ь': '-..-',
                    'э': '..-..',
                    'ю': '..--',
                    'я': '.-.-',
                    ' ': '',
                    '':' '}

frequency = 1000










window  = Tk()
window['bg']='gray22'
window.title('Морзе 3000')
window.geometry('500x500+500+200')
strv=StringVar()

lbl=Label(window,text='Привет! \n .--. .-. .. .-- . -',bg='gray22',fg='green',font=('Arial Bold',25))
lbl.place(relx=0.5,rely=0.25,anchor=CENTER)
btn1=Button(window,text='Преобразовать текст в Морзе',bg='gray23',fg='green',font=('Arial Bold',10),command=morse)
btn1.place(relx=0.25,rely=0.75,anchor=CENTER,)
btn2=Button(window,text='Преобразовать текст в Русский',bg='gray23',fg='green',font=('Arial Bold',10),command=MTR1)
btn2.place(relx=0.75,rely=0.75,anchor=CENTER)
vivod=Entry(window,bg='gray23',fg='green',width=35,font=('Arial Bold',15),textvariable=strv)
vivod.place(relx=0.5,rely=0.65,anchor=CENTER)
vivod.bind('.',tochka)
vivod.bind('-',tire)

window.mainloop()