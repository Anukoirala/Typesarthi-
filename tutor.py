import tkinter as tk
import tkinter.font as tkFont
import time
import front_page
import keyboard_layout
import second_page

global inc, start, stop
inc = 0
start = 0
stop = 0


# Updates the Label imported from text file whenever typed
# def update_label(keyevent):
#     # global inc
#     T.configure(text=data[inc:])


# records time after first and last keypress and then shows the average WPM
def update_time(keyevent):
    global inc, start, stop
    # print(keyevent.keycode)
    if inc == 1:
        start = time.time()
    elif inc == len(data):
        stop = time.time()
        speed=((len(data) / 5) / ((stop - start) / 60))
        label.config(text=speed)


# validates the data typed by the user in the entry box
def validate_data(S):
    global inc, start, stop
    if data[inc] == S:
        errmsg.config(text="")
        inc += 1
        return True
    else:
        return False


# Gets executed whenever wrong entry is given
def invalid_input(S):
    errmsg.config(text="Please try again.")


# Opens the contents of text file
with open('buttons.txt', 'r', encoding="utf-8") as myfile:
    data = myfile.read()


  # Main window
def window():
    global errmsg
    global T
    global screen5
    global label
    screen5 = tk.Frame(front_page.screen,width=300, height=300)
    screen5.pack()
    second_page.seconds.pack_forget()
    screen5.pack()

    # Font customization for displayed text
    costomFont = tkFont.Font(family='preeti', size=17)

    # back button
    b2 = tk.Button(screen5, text='BACK', command=second_page.tutorbaack)
    b2.pack()
    tk.Label(screen5, text='तल लेखिएकाे कुरा दाेहाेरयारनुहाेस्र').pack()

    # Command function binding for data validation
    vcmd = (screen5.register(validate_data), '%S')
    invcmd = (screen5.register(invalid_input), '%S')


    # Displays the contents of read text file as a label
    T = tk.Label(screen5, font=costomFont, text=data)
    T.pack()

    # Entry widget for typing area
    type_area = tk.Entry(screen5, validate="key", validatecommand=vcmd, invalidcommand=invcmd, font=costomFont)
    type_area.pack(pady=5, padx=5)
    type_area.focus_set()


    # Error message for invalid typing
    errmsg = tk.Label(screen5, text='', fg='red')
    errmsg.pack()


    keyboard_layout.tutor()

    # command function bindings for each keypress within the entry widget
    type_area.bind('<KeyPress>', keyboard_layout.shift_check)
    type_area.bind('<KeyRelease>', keyboard_layout.shift_uncheck)

    label = tk.Label(screen5, text='')
    label.pack()

    type_area.bind('<KeyRelease>', update_time,add='+')
    # type_area.bind('<KeyPress>', update_label, add='+')
