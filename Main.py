# Created 1-March-2016 by Jeremy Daugherty
# Main file for our Astral Calculator

"""
Astral Calculator's Main file, includes our windows and jumping off points for more windows.
"""

from tkinter import *
from tkinter import ttk
import pickle
import SolSys


# Utility functions to interface with the SolSys faster and nicer
def addbodyto(current, name, body, values):
    current.addbodyto(name, body)
    values['values'] = current.getnames()
    if '<None>' in values.get():
        values.set(body.Name)

    return


def changefocus(current, name):
    if '<None>':
        return

    return


# A dumb quick maker to test SolSys and outputting data to pickle
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

    check = data.addbodyto('Sun', temp)
    if check:
        print('It was added properly.')
    if temp is data.Bods:
        print('Something went wrong.')

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
current = SolSys.SolSys()

# Window setup
root = Tk()
root.title('Astral Calculator')
root.wm_iconbitmap('favicon.ico')
# End Setup

# Setup variables
SysName = StringVar()
SysName.set(current.Name)
CurrBod = StringVar()
CurrBod.set(current.getnames())
NewBodyNameVar = StringVar()

# What's in the Window
SystemLbl = Label(root, text='System Name')
SystemName = Entry(root, textvariable=SysName)
SystemName.bind('<Return>', lambda x: current.setname(SystemName.get()))
SystemName.bind('<FocusOut>', lambda x: current.setname(SystemName.get()))

BodyLBL = Label(root, text='Current Body')
BodyChoice = ttk.Combobox(root,
                          textvariable=CurrBod,
                          values=current.getnames(),
                          state='readonly'
                          )
BodyChoice.bind('<FocusOut>', lambda e: changefocus(current, CurrBod.get()))

NewBodyLBL = Label(root, text='New orbiting body')
NewBodyName = Entry(root, textvariable=NewBodyNameVar)
NewBodyButton = Button(root,
                       text='Create New Body',
                       command=lambda: addbodyto(current,
                                                 BodyChoice.get(),
                                                 SolSys.Body(NewBodyNameVar.get()),
                                                 BodyChoice
                                                         )
                       )

# Current Body Data, input, and output

# Save options
# Quick Save Button
QuickSaveButton = Button(root, text='QuickSave', command=lambda : pickle.dump(current, open('quicksave.p', 'wb')))


# Grid layout setting
SystemLbl.grid(row=0, column=0)
SystemName.grid(row=1, column=0, pady=4)

BodyLBL.grid(row=2, column=0, sticky=S)
BodyChoice.grid(row=3, column=0, sticky=N)

NewBodyLBL.grid(row=5, column=0)
NewBodyName.grid(row=6, column=0, pady=4)
NewBodyButton.grid(row=7, column=0, pady=4)

QuickSaveButton.grid(row=8, column=1, pady=4, padx=4)

if __name__ == "__main__":
    root.mainloop()
    print(current.Name)
    print(current.namesindict())
    print("You exist and should take comfort and that fact.")
