# Created 1-March-2016 by Jeremy Daugherty
# Main file for our Astral Calculator

"""
Astral Calculator's Main file, includes our windows and jumping off points for more windows.
"""

from tkinter import *
import SolSys

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello World\n(Click Me)"
        self.hi_there["command"] = self.say_hi

        self.QUIT = Button(self, text="QUIT", fg="red", command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("Hi there, everyone!")

root = Tk()
app = Application(master=root)
app.mainloop()

if __name__ == "__main__":
    print("You exist and should take comfort and that fact.")
