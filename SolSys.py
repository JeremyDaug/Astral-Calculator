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
        # Points to a body that will be treated as the Central most body (Such as the star)
        self.Heart = None
        # A dict of special traits, if empty assume heliocentric with no peculiarities
        self.Special = {}
        # Points to the body that is used as the measuring stick for all other systems in terms of this body's hr/day.
        self._Basis = None
        # Should contain a dict marked by degrees to give a rough backdrop over a year.
        self.Zodiac = {}

    def setbasis(self, base):
        if type(base) is Body:
            self._Basis = base
        else:
            raise Exception("Something Broke Somewhere")

    def getbasis(self):
        return self._Basis

    def sysday(self):
        if self._Basis is None:
            return 24
        else:
            return self._Basis.getday()


class Body:
    def __init__(self):
        self.Name = 'NA'  # The name of the body, should be unique, but is not required.
        self._Day = 24  # The length of the body's day in hours.
        self._Year = 0  # The length of the year in the body's day
        self._Start = 0  # The offset from 0 in degrees the body starts at
        self.Solstice = 0  # The day of the year that is counted as winter
        self.Special = {}  # A place holder Dict for oddity data, such as 90 Deg tilted planets and the like.
        self.Parent = None  # Points to the body it orbits, if empty it's the central planet
        self.Kids = []  # A list of bodies that orbit the body

    def day(self, num):
        """Data input/checker for _Day
        :param num: the number of hours in that day
        :return: Bool as to whether it is a valid input
        """
        if num < 0:
            return False
        else:
            self._Day = num
            return True

    def getday(self):
        return self._Day

    def year(self, num):
        """ Data input/checker for _year
        :param num: the number of hours in a year
        :return: Bool as to whether it is a valid input
        """
        if num < 0:
            return False
        else:
            self._Year = num
            return True

    def Start(self, num):
        """
        Data setter for _start
        :param num: The degree it is at (may be any number, but will be within [0,360)
        """
        self._Start = num % 360
