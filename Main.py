# Created 1-March-2016 by Jeremy Daugherty
# Main file for our Astral Calculator

"""
Astral Calculator's Main file, includes our windows and jumping off points for more windows.
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pickle
import SolSys
# import random

# A dumb quick maker to test SolSys and outputting data to pickle
def SolarSystemDefault(data=SolSys.SolSys()):
    # Create the universal system
    data.Name = 'Solar System'
    data.setday(24)

    # Sun
    temp = SolSys.Body()
    temp.Name = 'Sun'
    data.Bods = temp
    data.Current = data.Bods
    data.Extras['Ratio'] = SolSys.STDSOLRAT

    # Mercury
    temp = SolSys.Body(name='Mercury', year=88*24, day=175.97, extra={'Ratio': SolSys.STDTERRAT})
    data.addbodyto('Sun', temp)

    # Venus
    temp = SolSys.Body(name='Venus', year=225*24, day=117*24, extra={'Ratio': SolSys.STDTERRAT})
    data.addbodyto('Sun', temp)

    # Earth
    temp = SolSys.Body(name='Earth', year=365.25*24, day=24)
    data.addbodyto('Sun', temp)
    # Moon
    temp = SolSys.Body(name='Moon', year=29.5*24, day=29.5*24)
    data.addbodyto('Earth', temp)

    # Mars
    temp = SolSys.Body(name='Mars', year=687*24, day=24.617, extra={'Ratio': SolSys.STDTERRAT})
    data.addbodyto('Sun', temp)
    # Phobos
    temp = SolSys.Body(name='Phobos', year=0.318*24, day=0.318*24)
    data.addbodyto('Mars', temp)
    # Deimos
    temp = SolSys.Body(name='Deimos', year=1.236*24, day=1.236*24)
    data.addbodyto('Mars', temp)

    # Jupiter
    # Io
    # Europa
    # Ganymede
    # Callisto

    return data


# Window Class
class App:
    def __init__(self):
        # The star system we are working with.
        self.current = SolSys.SolSys()
        SolarSystemDefault(self.current)

        # Window setup
        self.root = Tk()
        self.root.title('Astral Calculator')
        self.root.wm_iconbitmap('favicon.ico')
        # End Setup

        # Setup variables
        self.SysName = StringVar()
        self.SysName.set(self.current.Name)
        self.CurrBod = StringVar()
        self.CurrBod.set(self.current.getnames()[0])
        self.NewBodyNameVar = StringVar()
        self.SystemDayVar = DoubleVar()
        self.SystemDayVar.set(self.current.Day)
        self.SystemYearVar = DoubleVar()
        self.SystemYearVar.set(self.current.Year)
        self.ParentRatioVar = DoubleVar()
        self.HarmRadioVar = IntVar()
        self.HarmRadioVar.set(1)

        self.CurrentBodyNameVar = StringVar()
        self.YearHourVar = IntVar()
        self.YearDayVar = DoubleVar()
        self.YearRadioVar = IntVar()
        self.DayVar = IntVar()
        self.OffsetVar = IntVar()
        self.ParentBodyVar = StringVar()
        if self.current.Current:
            if self.current.Current.Parent:
                self.ParentBodyVar.set(self.current.Current.Parent.Name)
        else:
            self.ParentBodyVar.set('<None>')
        self.DistVar = DoubleVar()
        self.RatioVar = DoubleVar()
        self.RatioDaysVar = DoubleVar()
        self.RatioDistVar = DoubleVar()

        # What's in the Window
        self.SystemLbl = Label(self.root, text='System Name')
        self.SystemName = Entry(self.root, textvariable=self.SysName)

        self.BodyLBL = Label(self.root, text='Current Body')
        self.BodyChoice = ttk.Combobox(self.root,
                                       textvariable=self.CurrBod,
                                       values=self.current.getnames(),
                                       state='readonly'
                                       )

        self.NewBodyLBL = Label(self.root, text='New orbiting body')
        self.NewBodyName = Entry(self.root, textvariable=self.NewBodyNameVar)
        self.NewBodyButton = Button(self.root,
                                    text='Create New Body',
                                    command=self.addbodyto)

        # Standard day of the System
        self.SystemDayLBL = Label(self.root, text='System Day Length')
        self.SystemDay = Entry(self.root, textvariable=self.SystemDayVar)

        # Standard year of the system
        self.SystemYearLBL = Label(self.root, text='System Year Length')
        self.SystemYear = Entry(self.root, textvariable=self.SystemYearVar)

        # Parents Data and harmonic ratio data
        self.ParentLBL = Label(self.root, text='Parent body')
        self.ParentLBL2 = Label(self.root, textvariable=self.ParentBodyVar)
        self.ParentRatioLBL = Label(self.root, text='Parent\'s Harmonic Ratio')
        self.ParentRatio = Label(self.root, textvariable=self.ParentRatioVar)
        # Radio buttons to change or maintain harmonic ratio, changing harmonic ratio effects all bodies.
        self.HarmRadio1 = Radiobutton(self.root, text='Maintain Harmonic Ratio', variable=self.HarmRadioVar, value=1)
        self.HarmRadio2 = Radiobutton(self.root, text='maintain Distance (Change Harmonic ratio)', value=2,
                                      variable=self.HarmRadioVar)


        # Current Body Data, input, and output
        # Body Name
        self.CurrentBodyLBL = Label(self.root, text='Body\'s name')
        self.CurrentBodyName = Entry(self.root, textvariable=self.CurrentBodyNameVar)

        # Year
        self.YearLBL = Label(self.root, text='Year')
        self.YearInHours = Label(self.root, text='Year in Hours')
        self.YearHour = Entry(self.root, textvariable=self.YearHourVar)
        self.YearInDay = Label(self.root, text='Year in System Days')
        self.YearDays = Entry(self.root, textvariable=self.YearDayVar)

        # Day
        self.DayLBL = Label(self.root, text='Day')
        self.DayInHours = Label(self.root, text='Day in Hours')
        self.DayHours = Entry(self.root, textvariable=self.DayVar)

        # Offset
        self.OffsetLBL = Label(self.root, text='Body Offset from 0 deg')
        self.Offset = Entry(self.root, textvariable=self.OffsetVar)

        # Distance from Parent
        self.DistLBL = Label(self.root, text='Distance in AUs')
        self.Dist = Entry(self.root, textvariable=self.DistVar)

        # Body Harmonic Ratio
        self.RatioLBL = Label(self.root, text='Harmonic Ratio')
        self.Ratio = Label(self.root, textvariable=self.RatioVar)
        self.RatioDaysLBL = Label(self.root, text='Change ratio by Days')
        self.RatioDays = Entry(self.root, textvariable=self.RatioDaysVar)
        self.RatioDistLBL = Label(self.root, text='Change Ratio By Distance in AUs')
        self.RatioDist = Entry(self.root, textvariable=self.RatioDistVar)

        # Children

        # Delete current Body
        self.DeleteCurr = Button(self.root,
                                 text='Delete Current Body',
                                 command=self.deletebody
                                 )

        # Save options
        # Quick Save Button
        self.QuickSaveButton = Button(self.root,
                                      text='QuickSave',
                                      command=lambda: pickle.dump(self.current, open('quicksave.p', 'wb')))
        self.QuickLoadButton = Button(self.root,
                                      text='QuickLoad',
                                      command=self.quickload)

        self.bindset()
        self.gridset()

        self.updatedata()
        return

    # Binding Settings
    def bindset(self):
        """"
        bindset, where al the binds are to be set. Organized by creation order
        """
        self.SystemName.bind('<Return>', lambda x: self.current.setname(self.SystemName.get()))
        self.SystemName.bind('<FocusOut>', lambda x: self.current.setname(self.SystemName.get()))

        self.BodyChoice.bind('<<ComboboxSelected>>', lambda e: self.updatedata())
        self.BodyChoice.bind('<Return>', lambda e: self.updatedata())
        self.BodyChoice.bind('<FocusOut>', lambda e: self.updatedata())

        self.NewBodyName.bind('<Return>', lambda e: self.addbodyto())

        self.SystemDay.bind('<Return>', self.changesysday)
        self.SystemDay.bind('<FocusOut>', self.changesysday)

        self.SystemYear.bind('<Return>', self.changesysyear)
        self.SystemYear.bind('<FocusOut>', self.changesysyear)

        self.CurrentBodyName.bind('<Return>', self.changename)
        self.CurrentBodyName.bind('<FocusOut>', self.changename)

        self.YearHour.bind('<FocusOut>', self.changeyearhours)
        self.YearHour.bind('<Return>', self.changeyearhours)
        self.YearDays.bind('<FocusOut>', self.changeyeardays)
        self.YearDays.bind('<Return>', self.changeyeardays)

        self.DayHours.bind('<FocusOut>', self.changedayhours)
        self.DayHours.bind('<Return>', self.changedayhours)

        self.Offset.bind('<Return>', self.changeoffset)
        self.Offset.bind('<FocusOut>', self.changeoffset)

        self.Dist.bind('<Return>', self.changedistance)
        self.Dist.bind('<FocusOut>', self.changedistance)
        return

    # Grid layout setting
    def gridset(self):
        SysLabGrd = (0, 0)  # 2x1
        BodChoGrd = (2, 0)  # 2x1
        NewBodGrd = (4, 0)  # 3x1
        SysDayGrd = (0, 1)  # 2x1
        SysYearGrd = (0, 2)  # 2x1
        ParentDataGrd = (1, 1)  # 5x1

        NewNameGrd = (3, 2)  # 1x2
        YearGrd = (4, 2)  # 3x2
        DayGrd = (7, 2)  # 2x2
        OffsetGrd = (6, 6)  # 2x2
        ParentGrd = (4, 6)  # 3x2
        RatGrd = (4, 8)  # 2x2
        DelGrd = (100, 0)  # 1x1
        QckSvGrd = (100, 100)  # 1x1

        self.SystemLbl.grid(row=SysLabGrd[0], column=SysLabGrd[1])
        self.SystemName.grid(row=SysLabGrd[0]+1, column=SysLabGrd[1], pady=4)

        self.BodyLBL.grid(row=BodChoGrd[0], column=BodChoGrd[1], sticky=S)
        self.BodyChoice.grid(row=BodChoGrd[0]+1, column=BodChoGrd[1], sticky=N)

        self.NewBodyLBL.grid(row=NewBodGrd[0], column=NewBodGrd[1])
        self.NewBodyName.grid(row=NewBodGrd[0]+1, column=NewBodGrd[1], pady=4)
        self.NewBodyButton.grid(row=NewBodGrd[0]+2, column=NewBodGrd[1], pady=4)

        self.SystemDayLBL.grid(row=SysDayGrd[0], column=SysDayGrd[1], padx=4, pady=4)
        self.SystemDay.grid(row=SysDayGrd[0]+1, column=SysDayGrd[1])

        self.SystemYearLBL.grid(row=SysYearGrd[0], column=SysYearGrd[1])
        self.SystemYear.grid(row=SysYearGrd[0]+1, column=SysYearGrd[1])

        self.ParentLBL.grid(row=ParentDataGrd[0], column=ParentDataGrd[1])
        self.ParentLBL2.grid(row=ParentDataGrd[0]+1, column=ParentDataGrd[1])
        self.ParentRatioLBL.grid(row=ParentDataGrd[0]+2, column=ParentDataGrd[1])
        self.ParentRatio.grid(row=ParentDataGrd[0]+3, column=ParentDataGrd[1])
        # Radio buttons to change or maintain harmonic ratio, changing harmonic ratio effects all bodies.
        self.HarmRadio1.grid(row=ParentDataGrd[0]+4, column=ParentDataGrd[1])
        self.HarmRadio2.grid(row=ParentDataGrd[0]+5, column=ParentDataGrd[1])

        # Unique to body.

        self.CurrentBodyLBL.grid(row=NewNameGrd[0], column=NewNameGrd[1])
        self.CurrentBodyName.grid(row=NewNameGrd[0], column=NewNameGrd[1]+1)

        self.YearLBL.grid(row=YearGrd[0], column=YearGrd[1])
        self.YearInHours.grid(row=YearGrd[0]+1, column=YearGrd[1])
        self.YearHour.grid(row=YearGrd[0]+1, column=YearGrd[1]+1)
        self.YearInDay.grid(row=YearGrd[0]+2, column=YearGrd[1])
        self.YearDays.grid(row=YearGrd[0]+2, column=YearGrd[1]+1)

        self.DayLBL.grid(row=DayGrd[0], column=DayGrd[1])
        self.DayInHours.grid(row=DayGrd[0]+1, column=DayGrd[1])
        self.DayHours.grid(row=DayGrd[0]+1, column=DayGrd[1]+1)

        self.DistLBL.grid(row=ParentGrd[0]+1, column=ParentGrd[1])
        self.Dist.grid(row=ParentGrd[0]+1, column=ParentGrd[1]+1)

        self.OffsetLBL.grid(row=OffsetGrd[0], column=OffsetGrd[1])
        self.Offset.grid(row=OffsetGrd[0], column=OffsetGrd[1]+1)

        self.RatioLBL.grid(row=RatGrd[0], column=RatGrd[1])
        self.Ratio.grid(row=RatGrd[0], column=RatGrd[1]+1)
        self.RatioDaysLBL.grid(row=RatGrd[0]+1, column=RatGrd[1])
        self.RatioDays.grid(row=RatGrd[0]+1, column=RatGrd[1]+1)
        self.RatioDistLBL.grid(row=RatGrd[0]+2, column=RatGrd[1])
        self.RatioDist.grid(row=RatGrd[0]+2, column=RatGrd[1]+1)

        self.DeleteCurr.grid(row=DelGrd[0], column=DelGrd[1])

        self.QuickSaveButton.grid(row=QckSvGrd[0], column=QckSvGrd[1], pady=4, padx=4)
        self.QuickLoadButton.grid(row=QckSvGrd[0]+1, column=QckSvGrd[1], pady=4, padx=4)

    def addbodyto(self):
        if self.NewBodyNameVar.get() == '':
            messagebox.showwarning('New Body Creation Error', 'No name given, no body made.')
            return
        temp = SolSys.Body(name=self.NewBodyNameVar.get())
        self.current.addbodyto(self.CurrBod.get(), temp)
        self.BodyChoice['values'] = self.current.getnames()
        if '<None>' in self.BodyChoice.get():
            self.BodyChoice.set(temp.Name)
            self.current.Current = temp
        self.NewBodyNameVar.set('')
        self.updatedata()
        return

    def updatedata(self):
        if self.current.Current is None:
            return
        self.current.setcurrent(self.CurrBod.get())
        self.CurrentBodyNameVar.set(self.CurrBod.get())
        self.YearHourVar.set(self.current.Current.Year)
        self.YearDayVar.set(self.current.Current.Year/self.current.Day)
        self.DayVar.set(self.current.Current.Day)
        if self.current.Current.Parent is None:
            self.ParentBodyVar.set('<None>')
        else:
            self.ParentBodyVar.set(self.current.Current.Parent.Name)
        self.OffsetVar.set(self.current.Current.Offset)
        self.DistVar.set(self.current.orbitdistance())
        self.RatioVar.set(self.current.Current.getparentratio())
        self.RatioDaysVar.set(self.current.Current.Year)
        self.RatioDistVar.set(self.current.orbitdistance())
        return

    def changename(self, event=None):
        if self.CurrentBodyNameVar.get() != self.CurrBod.get():
            self.current.Current.Name = self.CurrentBodyNameVar.get()
            self.BodyChoice['values'] = self.current.getnames()
            self.CurrBod.set(self.CurrentBodyNameVar.get())
        return

    def changeyearhours(self, event=None):
        self.current.Current.setyear(self.YearHourVar.get())
        self.updatedata()
        return

    def changeyeardays(self, event=None):
        self.current.Current.setyear(self.YearDayVar.get()*self.current.Day)
        self.updatedata()
        return

    def changedayhours(self, event=None):
        self.current.Current.setday(self.DayVar.get())
        self.updatedata()
        return

    def changesysday(self, event=None):
        if not self.current.setday(self.SystemDayVar.get()):
            messagebox.showwarning('Invalid Range for Day', 'Must be a positive Value')
            return
        self.updatedata()
        return

    def changesysyear(self, event=None):
        if not self.current.setyear(self.SystemYearVar.get()):
            messagebox.showwarning('Invalide Range For Year', 'Must be a Non-negative Value')
        self.updatedata()
        return

    def changeoffset(self, event=None):
        self.current.Current.setoffset(self.OffsetVar.get())
        return

    def quickload(self, event=None):
        self.current = pickle.load(open('quicksave.p', 'rb'))
        self.CurrBod.set(self.current.Current.Name)
        self.updatedata()
        return

    def deletebody(self):
        if self.current.Current is None:
            messagebox.showwarning('Body Delete Error', 'No body to Delete')
        elif not self.current.Current.children:
            self.current.Current = self.current.deletebody(self.current.Current)
            if self.current.Current is None:
                self.current.Bods = None
            self.updatedata()
            self.BodyChoice['values'] = self.current.getnames()
            if '<None>' in self.BodyChoice.get():
                self.BodyChoice.set('<None>')
            self.CurrBod.set(self.BodyChoice['values'][0])
        elif self.current.Current.children:
            messagebox.showwarning('Body Delete Error', 'Body has children, delete them first')
        return

    def changedistance(self, event=None):
        self.current.changedistance(distance=self.DistVar.get(), name=self.CurrBod.get())
        self.updatedata()
        return


if __name__ == "__main__":
    Root = App()
    Root.root.mainloop()
    print(Root.current.Day)
    print(Root.current.Year)
    print(Root.current.namesindict())
    print("You exist and should take comfort and that fact.")
