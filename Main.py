# Created 1-March-2016 by Jeremy Daugherty
# Main file for our Astral Calculator

"""
Astral Calculator's Main file, includes our windows and jumping off points for more windows.
"""

from tkinter import *
import json
from tkinter import ttk
from tkinter import messagebox
import SolSys


# A dumb quick maker to test SolSys and outputting data to a json
def SolarSystemDefault(data=SolSys.SolSys()):
    # Create the universal system
    data.Name = 'Solar System'
    data.Zodiac = {}

    # Create the sun
    heart = SolSys.Body()
    heart.Name = 'Sun'
    heart.day(11)
    heart.Special['Central'] = True
    data.Heart = heart
    data.Special['Helio'] = True
    core = SolSys.Body()
    core.Name = 'Earth'
    core.day(24)
    core.year(365.25)
    core.Parent = data.Heart
    data.setbasis(core)
    data.Heart.Kids.append(core)

    return data

# Our Current Solar System that we are working through.
current = SolSys.SolSys()
SolarSystemDefault(current)


# Window setup
root = Tk()
root.title('Astral Calculator')
root.wm_iconbitmap('favicon.ico')
# End Setup

# What's in the Window
SystemLbl = Label(root, text='System Name').grid(row=0, column=0)
SystemName = Entry(root).grid(row=1, column=0)
CoreLBL = Label(root, text='Core Object\'s Name').grid(row=0, column=1)
CoreName = Entry(root).grid(row=1, column=1)
CoreDayLBL = Label(root, text='Core Object\'s Day in hours').grid(row=3)
CoreDay = Entry(root).grid(row=4)
btn = Button(root, text='Button').grid(row=5)

if __name__ == "__main__":
    root.mainloop()
    print("You exist and should take comfort and that fact.")
