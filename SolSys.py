# Solar System Data Container and most of the calculation work.
# Part of the Astral Calculator
# Contains the Classes and functions for SolSys and Body

# from math import *


class SolSys:
    """
    Solar System Class
    Holds all data and acts as both an interface and manager for our celestial bodies.
    """
    def __init__(self):
        # The name of the system
        self.Name = ''
        # The tree of the system
        self.Bods = None
        # The standardized day of the system
        self.Day = 24
        # The body we are currently observing
        self.Current = None

    def setday(self, num):
        """
        Sets the system's standard day unit in hours to standardize the year in days across the system.
        :param num: The number of hours in the day
        """
        if num < 0:
            self.Day = -num
        else:
            self.Day = num

    def basedayoff(self, bod):
        """
        Sets the System's day off of a given body's day.
        :param bod: The body we are basing our day off of.
        """
        self.Day = bod.Day

    def getnames(self):
        """
        Gets a list of all the bodies names and outputs them in a list
        :return: A lizt of strings, all the names of the existing bodies.
        """
        if self.Bods is None:
            return ['<None>']

        ret = list()
        self.Bods.getnames(ret)
        return ret

    def addbodyto(self, name, body):
        """
        Adds a body to the body of the given name
        :param name: The name of the body to add to
        :param body: The Body to be added
        :return: Bool of success or failure.
        """
        if self.Bods is None:
            print('No body exists!')
            self.Bods = body
        return self.Bods.addbodyto(name, body)

    def namesindict(self):
        """
        Returns a dict form of all names, arranged in a basic tree shape.
        :return: A dict structure all the way down.
        """
        if self.Bods is None:
            return 'None'
        ret = {}
        self.Bods.namesindict(ret)
        return ret

    def setname(self, name):
        self.Name = name
        return


class Body:
    """
    Body Class
    Holds all data for our celestial bodies.
    """
    def __init__(self, name=''):
        # Name of the body
        self.Name = name
        # Length of the year in hours
        self.Year = 0
        # length of the day in hours
        self.Day = 24
        # offset from 0 that it start around the planet
        self.Offset = 0
        # the body it orbits about.
        self.Parent = None
        # The children of the body that orbit it.
        self.children = []

    def setyear(self, num):
        """
        Set the year of the body
        :param num: the length of the year, automatically makes it positive.
        """
        if num < 0:
            self.Year = -num
        else:
            self.Year = num

    def setday(self, num):
        """
        Sets the length of the planet's day in hours
        :param num: The amount of hours in a day, automatically made positive
        """
        if num < 0:
            self.Day = -num
        else:
            self.Day = num

    def setoffset(self, num):
        """
        Sets the offset of the body from 0 that it's at.
        :param num: the number that is put into the offset, modded to be between 0 and 360
        """
        self.Offset = num % 360

    def getnames(self, ret):
        ret.append(self.Name)
        for i in self.children:
            i.getnames(ret)

    def addbodyto(self, name, body):
        if self.Name == name:
            body.Parent = self
            self.children.append(body)
            return True

        for i in self.children:
            if i.addbodyto(name, body):
                return True

        return False

    def namesindict(self, ret):
        ret[self.Name] = {}
        for i in self.children:
            i.namesindict(ret[self.Name])
