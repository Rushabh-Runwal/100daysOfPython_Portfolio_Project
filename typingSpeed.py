# Link Hello world import letter tomato navigate mainly ghost runner sporty sport shoes shorts wear clothes wallet cap type speed fresh teach terminal tunnel run fast slow project sit stand walk runLay over sleep mother on together dad look by family fighting try me top upcoming new my texts my favorites create text improve your typing America Speed Language English become forum feedback contact supporter FAQ open chat typing test top 200 words typing test advanced top 1000 words custom typing test create your own multiplayer typing test play against others typing competition wh can type the fastest text practice practice your own text

from tkinter import *
import random
import time
from tkinter import messagebox


class TypingSpeed:
    def __init__(self):
        self.words = 'Link Hello world import letter tomato navigate mainly ghost runner sporty sport shoes shorts ' \
                     'wear clothes wallet cap type speed fresh teach terminal tunnel run fast slow project sit stand ' \
                     'walk runLay over sleep mother on together dad look by family fighting try me top upcoming new ' \
                     'my texts my favorites create text improve your typing America Speed Language English become ' \
                     'forum feedback contact supporter FAQ open chat typing test top 200 words typing test advanced ' \
                     'top 1000 words custom typing test create your own multiplayer typing test play against others ' \
                     'typing competition wh can type the fastest text practice practice your own text'.split()
        self.total, self.score_count = 0, 0
        self.t_end = None
        self.input_word, self.ran_word = "", ""

        self.window = Tk()
        self.window.geometry("480x240+300+200")
        self.window.title("Let's Check Your typing Speed")
        self.window.config(padx=10, pady=10)

        self.canvas = Canvas(width=460, height=220, highlightthickness=0)
        self.word = self.canvas.create_text(115, 15, text="Press START", fill="black", font=('times 20', 24, "bold"))
        self.w = self.canvas.create_text(150, 40, text="(press Space to go next word)", fill="black",
                                         font=('times 20', 12, "bold"))
        self.canvas.place(x=35, y=30)

        self.entry = Entry(self.window, font=('times 20', 18, "bold"))
        self.entry.place(x=35, y=90)

        self.Score = Label(self.window, text=f"Score: {self.score_count}", font=('times 20', 14, "bold"))
        self.Score.place(x=35, y=140)

        self.st_btn = Button(text="START", highlightthickness=0, command=self.generate, font=('times 20', 12, "bold"))
        self.st_btn.place(x=200, y=180)

        self.window.mainloop()

    def generate(self):
        self.st_btn["state"] = "disabled"
        self.entry.delete(0, END)
        if not self.t_end:
            self.t_end = time.time() + 60
        elif time.time() > self.t_end:
            wrong = self.total - self.score_count
            msg = f"Speed: {self.score_count} words/minute\n\nmistake/s: {wrong}"
            messagebox.showinfo("Typing Speed result", msg)
            return

        self.entry.focus()
        self.ran_word = random.choice(self.words)
        self.canvas.itemconfig(self.word, text=self.ran_word)
        self.window.bind('<space>', self.clicked, )

    def clicked(self, e):
        self.input_word = self.entry.get().replace(" ", "")
        self.total += 1
        if self.input_word == self.ran_word:
            self.score_count += 1
            self.Score.config(text=f"Score: {self.score_count}")
        self.generate()


obj = TypingSpeed()
