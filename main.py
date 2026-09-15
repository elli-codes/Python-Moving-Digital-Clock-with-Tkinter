from tkinter import *
import time

class my_class:

    def __init__(self):

        self.n = 0

        self.root = Tk()

        self.root.geometry("300x100+%d+700" % self.n)
        self.root.overrideredirect(True)
        self.root.config(bg="#555555")
        self.root.wm_attributes("-alpha", 0.6)
        self.root.wm_attributes("-topmost",True)

        self.txt1 = Label(
            self.root,
            text="",
            bg="#555555",
            fg="white",
            font=("Impact", 50)
        )

        self.txt1.pack(expand=True, fill="both")

        self.update_clock()

        self.root.after(500, self.move)

        self.root.mainloop()

    def update_clock(self):

        self.txt1.config(
            text=time.strftime("%H:%M:%S")
        )

        self.root.after(1000, self.update_clock)

    def move(self):

        self.n += 50

        if self.n >= self.root.winfo_screenwidth():
            self.n = -300

        self.root.geometry("300x100+%d+700" % self.n)

        self.root.after(500, self.move)


if __name__ == "__main__":
    my_class()
