# Author:Anupama Koirala

import tkinter as tk
import tkinter.font as tkfont


import front_page

import second_page
import Test


def tutor():
    global screen3

    screen3 = tk.Frame(front_page.screen, width=300, height=300)
    screen3.pack(padx=20, pady=20)
    screen3.focus_set()
    keyboard()


def test():
    global screen3

    screen3 = tk.Frame(front_page.screen, width=400, height=50)
    screen3.pack(padx=20, pady=20)
    second_page.seconds.pack_forget()
    screen3.focus_set()
    keyboard()


shift_check_bool = False


def shift_check(keyevent):
    global shift_check_bool
    if keyevent.keycode == 50 and shift_check_bool == False :
        shift()
        shift_check_bool = True


def shift_uncheck(keyevent):
    global shift_check_bool
    if keyevent.keycode == 50:
        keyboard()
        shift_check_bool = False


buttons = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
           'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'BACK',
           'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", '\ ', 'ENTER',
           'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'SHIFT', 'SPACE']

bottons=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
         'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', 'BACK',
         'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', '|', 'ENTER',
         'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', 'SHIFT', 'SPACE'
         ]


def shift():
    global b1
    customFont = tkfont.Font(family='preeti', size=17)

    varRow = 1
    varColumn = 0

    for botton in bottons:

        # commands = lambda x=botton: key(x)

        if botton == 'SPACE' or botton == 'SHIFT' or botton == 'BACK' or botton == 'ENTER':
            b1 = tk.Button(screen3, text=botton, width=10, padx=1, pady=1,bd=1,relief='raised')
            b1.grid(row=varRow, column=varColumn)
            # b1.bind('<KeyPress>',lambda e: commands())

        else:
            b2 = tk.Button(screen3, text=botton, width=10, padx=1, pady=1, bg='WHITE', bd=1,
                         relief='raised',font=customFont)
            b2.grid(row=varRow, column=varColumn)
            # b2.screen3.bind('<KeyPress>',lambda e: commands(), add='+')


        varColumn += 1
        if varColumn > 11 and varRow == 1:
            varColumn = 0
            varRow += 1
        if varColumn > 12 and varRow == 2:
            varColumn = 0
            varRow += 1
        if varColumn > 12 and varRow == 3:
            varColumn = 0
            varRow += 1


def keyboard():
    varrow=1
    varcolumn=0
    customFont = tkfont.Font(family='preeti', size=17)

    for button in buttons:
        # command = lambda x=button: select(x)

        if button == 'SPACE' or button == 'SHIFT' or button == 'BACK' or button=='ENTER':
            b3 = tk.Button(screen3, text=button, width=10, padx=1, pady=1, bg='GREY', bd=1, relief='raised',
                           activebackground='WHITE')
            b3.grid(row=varrow, column=varcolumn)
            # b3.screen3.bind('<KeyPress>', lambda e: command(), add='+')

        else:

            b4 = tk.Button(screen3, text=button, width=10, padx=1, pady=1,bg='GREY', bd=1, relief='raised',
                         activebackground='WHITE',font=customFont)
            b4.grid(row=varrow, column=varcolumn)
            # b4.screen3.bind('<KeyPress>',lambda e: command(), add='+')


        varcolumn += 1
        if varcolumn > 11 and varrow == 1:
            varcolumn = 0
            varrow += 1
        if varcolumn > 12 and varrow == 2:
            varcolumn = 0
            varrow += 1
        if varcolumn > 12 and varrow == 3:
            varcolumn = 0
            varrow += 1


# def main():
#     # tk.Label(screen3, text='   ').grid(row=0, columnspan=20)
#     global entry
#     # entry = tk.Entry(screen3, width=90)
#     # entry.grid(row=0, columnspan=20)


