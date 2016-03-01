# Solar System Data Container and most of the calculation work.
# Part of the Astral Calculator
# Contains the Classes and functions for SolSys and Body

# from math import *


class SolSys:
    """
    Solar System Class
    Holds all data and acts as both an interface and manager for our celestial bodies.

    Name: The name of the system to be output elsewhere.
    _Heart: The body that is being used as the central most pivot point.
    _Special: A Special container that holds data for system wide oddities.
    """
    def __init__(self):
        """
        Initializer, takes nothing and makes nothing real. Adds in new stuff for init but nothing useful.

        :return: Returns the created class
        """
        self.Name = "Unnamed"
        self.Heart = None  # Points to a body that will be treated as the Central most body (Such as the star)
        self.Special = {}  # A dict of special traits, if empty assume heliocentric with no peculiarities

        # Points to the body that is used as the measuring stick for all other systems in terms of this body's hr/day.
        self._Basis = None
        self._Zodiac = {}  # Should contain a dict marked by degrees to give a rough backdrop over a year.

    def core(self, title, body_name):
        """
        Adds in the central most body of the system and it's data.
        :param title: The name of the system.
        :param body_name: The name of the body at the center.
        """
        self.Name = title
        self.Heart = Body()
        self.Heart.Name = body_name
        self.Heart.changeday(int(input("How long of a day (in hours) does it have, if any. (Must be Non-negative)"
                                       "Hours: ")))


class Body:
    def __init__(self):
        self.Name = 'NA'  # The name of the body, should be unique, but is not required.
        self.Day = 24  # The length of the body's day in hours.
        self.Year = 0  # The length of the year in the body's day
        self.Start = 0  # The offset from 0 in degrees the body starts at
        self.Solstice = 0  # The day of the year that is counted as winter
        self.Special = {}  # A place holder Dict for oddity data, such as 90 Deg tilted planets and the like.
        self.Parent = None  # Points to the body it orbits, if empty it's the central planet
        self.Kids = None  # A list of bodies that orbit the body

    def changeday(self, time):
        while time < 0:
            print("Try again, and put in a number at least equal to 0 this time.")
            time = int(input("Hours: "))

        self.Day = time
        if time == 0:
            self.Special['Dayless'] = True
