# Created 1-March-2016 by Jeremy Daugherty
# Main file for our Astral Calculator

"""
Astral Calculator's Main file, includes our windows and jumping off points for more windows.
"""

from tkinter import *
from tkinter import ttk
import pickle
import SolSys


# A dumb quick maker to test SolSys and outputting data to a json
def SolarSystemDefault(data=SolSys.SolSys()):
    # Create the universal system
    data.Name = 'Solar System'
    data.setday(24)

    # Sun
    temp = SolSys.Body()
    temp.Name = 'Sun'
    data.Bods = temp

    if temp is data.Bods:
        print('temp and data.Bods is the same')

    # Earth
    temp = SolSys.Body()
    temp.Name = 'Earth'
    temp.Year = 365.25 * 24
    temp.Day = 24
    temp.Parent = data.Bods
    data.Bods.children.append(temp)

    temp = SolSys.Body()
    temp.Name = 'Moon'
    temp.Year = 29.5
    temp.Day = 29.5

    check = data.addbodyto('Earth', temp)
    if check:
        print('It was added properly')

    if temp is data.Bods:
        print('Yeah, this shit needs to be fixed')

    pickle.dump(data, open('test.p', 'wb'))

    print(data.getnames())
    print(data.namesindict())

    return data

# Our Current Solar System that we are working through.
SolarSystemDefault()
current = pickle.load(open('test.p', 'rb'))


# Window setup
root = Tk()
root.title('Astral Calculator')
root.wm_iconbitmap('favicon.ico')
# End Setup

# Setup variables

# What's in the Window
SystemLbl = Label(root, text='System Name').grid(row=0, column=0)
SystemName = Entry(root).grid(row=1, column=0)

BodyChoice = ttk.Combobox(root, values=current.getnames()).grid(row=2, column=0)

NewBodyLbl = Button(root, text='New Body').grid(row=3, column=0)

# Current Body Data, input, and output

if __name__ == "__main__":
    root.mainloop()
    print("You exist and should take comfort and that fact.")
