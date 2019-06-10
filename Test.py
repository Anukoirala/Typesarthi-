# Author:Anupama Koirala

import tkinter as tk
import tkinter.font as tkfont
import front_page
import second_page
import time

import keyboard_layout

inc = 0
start = 0
stop = 0
i = 2
s = 0

with open('text', 'r', encoding="utf-8") as file:
    data = file.read()

m = len(data)
print(m)


def update_time(keyevent):
    global inc, start, stop
    global s

    if inc == 1:
        start = time.time()

    elif inc == m:
        stop = time.time()
        s = ((len(data) / 5) / ((stop - start) / 60))
          # s=(stop-start)/inc
        # time_label.config(text=s)
        typ.destroy()
        t.destroy()
        keyboard_layout.screen3.pack_forget()
        time_label.destroy()
        errmssg.destroy()
        # screen4.pack()
        label = tk.Label(screen4, height=300, width=400, text="Congratulations!! Your speed is " + str(s))
        label.pack()
        speed = tk.Label(screen4, text = str(s))
        speed.pack()
        print(s)


def main():
    global errmssg
    global time_label
    global screen4
    global typ
    global t
    screen4 = tk.Frame(front_page.screen, width=300, height=300)
    screen4.pack()
    second_page.seconds.pack_forget()

    customFont = tkfont.Font(family='preeti', size=17)
    vcmd = (screen4.register(validate_data), '%S')
    invcmd = (screen4.register(invalid_data), '%S')

    t = tk.Text(screen4, height=4, width=50, fg='BlUE', font = customFont)
    t.insert(0.0, data)
    t.config(state='disabled')
    t.pack()

    typ = tk.Entry(screen4, validate="key", validatecommand=vcmd, invalidcommand=invcmd, font = customFont)
    typ.pack()
    typ.focus_set()

    errmssg = tk.Label(screen4, text=" ")
    errmssg.pack()
    b = tk.Button(screen4, text='BACK', command=second_page.testback)
    b.pack()
    keyboard_layout.test()

    typ.bind('<KeyPress>', keyboard_layout.shift_check)
    typ.bind('<KeyRelease>', keyboard_layout.shift_uncheck)
    typ.bind('<KeyRelease>', update_time,add='+')


    time_label = tk.Label(screen4, text='')
    time_label.pack()


def validate_data(S):
    global inc, i
    if data[inc] == S:
        errmssg.config(text=" ")
        inc += 1
        # update_time()
        # i += 1
        # if i == m:
        #    text()
        return True
    else:
        return False


def invalid_data(S):
    errmssg.config(text='Please try again ', fg='red')

# def text():
#     global i, m
#     i += 1
#     if i >= m:
#         typ.destroy()
#         t.destroy()
#         keyboard_layout.screen3.pack_forget()
#         time_label.destroy()
#         errmssg.destroy()
#         # screen4.pack()
#         label = tk.Label(screen4, height=300, width=400, text="Congratulations!! Your speed is ")
#         label.pack()
#         l=tk.Label(screen4,text=s)
#         l.pack(side=tk.LEFT)


