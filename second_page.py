# Author:Anupama Koirala

from tkinter import *
import tkinter.font as tkfont


import front_page

import tutor
import game
import keyboard_layout

import Test

# customFont = tkfont.Font(family='preeti', size=17)

def second():
    global seconds
    seconds = Frame(front_page.screen, width=300, height=300)
    seconds.pack(padx=20, pady=20)

    front_page.front.pack_forget()
    front_page.screen1.pack_forget()
    front_page.screen2.pack_forget()

    seconds.pack(padx=20, pady=20)
    l1 = Label(seconds, text='6fOk;f/yL', font='kantipur')
    l1.pack()

    b1 = Button(seconds, text='v]n', width=7, height=1, command=game_call, font = 'kantipur')
    b1.pack(side=RIGHT, padx=10, pady=10, expand=False)
    b1.focus_set()
    # b1.bind('<Return>', lambda dummy=0: call(), add='+')


    b2 = Button(seconds, text="6\o'6/", width=7, height=1, command=call, font = 'kantipur')
    b2.pack(side=RIGHT, padx=0, pady=10, expand=False)
    # b2.bind('<Return>', lambda dummy=0: call(), add='+')

    b3 = Button(seconds,text='hfFr', width=7,height=1, command=testcall, font = 'kantipur')
    b3.pack(side=RIGHT, padx=10, pady=10, expand=False)
    # b3.bind('<Return>', lambda dummy=0: call(), add='+')


def call():
    tutor.window()
    # print('hlw')

def testcall():
    # keyboard_layout.test()
    Test.main()
def game_call():
    game.main()
    # print("hi")

def testback():
    Test.screen4.pack_forget()
    # tutor.screen5.pack_forget()
    keyboard_layout.screen3.pack_forget()
    # seconds.pack(padx=20,pady=20)
    second()

def tutorbaack():
    tutor.screen5.pack_forget()
    keyboard_layout.screen3.pack_forget()
    second()






