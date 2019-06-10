import tkinter as tk
import random
import front_page
import second_page

xLoc = 00
yLoc = 00
i = 0
j = 0
b = 0
m = 0


class Text1:

    def __init__(self, canvas1, xLoc, yLoc, word):
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.canvas = canvas1
        self.word = word
        self.id = canvas1.create_text(xLoc, yLoc, text=word, font = ('preeti', 20))

    def move_text(self):
        deltax = 5
        deltay = 5
        bbox = canvas.bbox(self.id)
        if bbox[0] >= 300:
            canvas.delete('all')
            del_entry()
            canvas.create_text(150, 150, text='Level 1 Failed')

        else:
            self.canvas.move(self.id, deltax, deltay)
            self.canvas.after(100, self.move_text)

    def del_text(self):
        global b
        b += 1
        self.canvas.delete(b)


def show_score():
    canvas.create_text(150, 150, text='Congratulations, You have completed level 1')


def main():
    global app
    global screen7
    global canvas
    global xLoc
    global yLoc
    global text1
    global easy_words
    global m

    screen7 = tk.Frame(front_page.screen, width=300, height=300)
    screen7.pack()
    canvas = tk.Canvas(screen7, width=300, height=300, bg = 'silver')
    canvas.pack()

    second_page.seconds.pack_forget()
    screen7.pack()
    with open("easy_words.txt") as f:
        easy_words = list(map(lambda s: s.strip('\n'), f.readlines()))
        random.shuffle(easy_words)
    for k, w in enumerate(easy_words):
        text1 = Text1(canvas, xLoc, yLoc, w)
        xLoc = xLoc - 300
        yLoc = yLoc - 300
        text1.move_text()

        m = len(easy_words)
    app = KeyValidationDemo()



def delete():
    text1.del_text()


def del_entry():
    print("HHHHHH")
    app.del_entries()


def final_score():
    show_score()


class KeyValidationDemo:
    def __init__(self):
        self.vcmd = (screen7.register(self.validate_data), '%S')
        self.invcmd = (screen7.register(self.invalid_name), '%S')
        self.entry = tk.Entry(screen7, validate="key", validatecommand=self.vcmd, invalidcommand=self.invcmd, font = ('preeti', 15))
        self.entry.pack(pady=5, padx=5)
        self.entry.focus_set()
        self.errmsg = tk.Label(screen7, text='', fg='red')
        self.errmsg.pack()

    def validate_data(self, S):
        global i, j, m
        self.errmsg.config(text='')
        if easy_words[i][j] == S and len(easy_words[i]) > j:
            j += 1
            if len(easy_words[i]) == j:
                j = 0
                i += 1
                delete()
                self.delete_entry()
                m -= 1
                return True
            return True
        else:
            return False

    def invalid_name(self, S):
        self.errmsg.config(text='Invalid characters \n name can only have alphabets')

    def delete_entry(self):
        global app
        self.entry.delete(0, 'end')
        self.entry.destroy()
        self.errmsg.destroy()
        if m > 1:
           app = KeyValidationDemo()
        else:
            final_score()

    def del_entries(self):
        print('JJJJ')
        self.entry.destroy()
        print('KKKK')
        self.errmsg.destroy()


