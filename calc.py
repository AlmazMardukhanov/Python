import tkinter
from tkinter import *
def q():
    return c.set(c.get() + '1')
def w():
    return c.set(c.get() + '+')
def e():
    return c.set(c.get() + '2')
def r():
    return c.set(c.get() + '3')
def t():
    return c.set(c.get() + '4')
def y():
    return c.set(c.get() + '5')
def u():
    return c.set(c.get() + '6')
def i():
    return c.set(c.get() + '7')
def o():
    return c.set(c.get() + '8')
def p():
    return c.set(c.get() + '9')
def a():
    return c.set(c.get() + '-')
def s():
    return c.set(c.get() + '**')
def z():
    return c.set(c.get() + '(')
def x():
    return c.set(c.get() + ')')
def d():
    return c.set(c.get() + '*')
def h():
    return c.set('')
def j():
    return c.set(c.get() + '/')
def tochka():
    return c.set(c.get()+'.')
def null():
    return c.set(c.get()+'0')

def ravn():
    return c.set(eval(c.get()))


window = Tk()
window.title("Калькулятор")
window.geometry('300x321')
c = StringVar()
knopka1 = tkinter.Button(window, text = "1",width=6, height=4,command = q)
knopka1.place(x=0,y=50)
knopka2 = tkinter.Button(window, text = "2",width=6, height=4,command = e)
knopka2.place(x=50,y=50)
knopka3 = tkinter.Button(window, text = "3",width=6, height=4,command = r)
knopka3.place(x=90,y=50)
knopka4 = tkinter.Button(window, text = "4",width=6, height=4,command = t)
knopka4.place(x=0,y=115)
knopka5 = tkinter.Button(window, text = "5",width=6, height=4,command = y)
knopka5.place(x=45,y=115)
knopka6 = tkinter.Button(window, text = "6",width=6, height=4,command = u)
knopka6.place(x=90,y=115)
knopka7 = tkinter.Button(window, text = "7",width=6, height=4,command = i)
knopka7.place(x=0,y=180)
knopka8 = tkinter.Button(window, text = "8",width=6, height=4,command = o)
knopka8.place(x=45,y=180)
knopka9 = tkinter.Button(window, text = "9",width=6, height=4,command = p)
knopka9.place(x=90,y=180)
knopka10 = tkinter.Button(window, text = "=",width=6, height=4,command = ravn)
knopka10.place(x=135,y=50)
knopka11 = tkinter.Button(window, text = "+",width=6, height=4,command = w)
knopka11.place(x=135,y=115)
knopka12 = tkinter.Button(window, text = "-",width=6, height=4,command = a)
knopka12.place(x=135,y=180)
knopka13 = tkinter.Button(window, text = "*",width=6, height=4,command = d)
knopka13.place(x=185,y=50)
knopka14 = tkinter.Button(window, text = "/",width=6, height=4,command = j)
knopka14.place(x=185,y=115)
knopka15 = tkinter.Button(window, text = "(",width=6, height=4,command = z)
knopka15.place(x=185,y=180)
knopka16 = tkinter.Button(window, text = "с",width=6, height=4,command = h)
knopka16.place(x=235,y=50)
knopka17 = tkinter.Button(window, text = "**",width=6, height=4,command = s)
knopka17.place(x=235,y=115)
knopka15 = tkinter.Button(window, text = ")",width=6, height=4,command = x)
knopka15.place(x=235,y=180)
knopka18=tkinter.Button(window,text=".",width=6, height=4,command=tochka)
knopka18.place(x=90,y=250)
knopka19=tkinter.Button(window,text="0",width=6, height=4,command=null)
knopka19.place(x=45,y=250)
pole = tkinter.Entry(window,width =40, textvariable = c)
pole.place(x=15,y=10)

window.mainloop()