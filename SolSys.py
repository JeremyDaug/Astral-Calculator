"""
Solar System Data Container and most of the calculation work.
Part of the Astral Calculator
Contains the Classes and functions for SolSys and Body
"""

from math import *

# Constants for our defaults
AU = 1.4960 * 10 ** 11  # 1 AU = X in meters
# Law of Harmonies Time**2 / Radius**3 unique to every dominating body with children
# To be more exact Hours**2 / AU**3
STDSOLRAT = ((365.25*24)**2)/(1**3)  # Based on Sun/Earth
STDTERRAT = ((29.5*24)**2)/(0.0026**3)  # Based on Earth/Moon
STDGASRAT = ((1.77*24)**2)/((421700/AU)**3)  # Based on Jupiter/Io


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
        # The standardized Year of the System
        self.Year = 365
        # The body we are currently observing
        self.Current = None
        # Extra Data that is used by the system in total.
        self.Extras = {}

    def setday(self, num):
        """
        Sets the system's standard day unit in hours to standardize the year in days across the system.
        :param num: The number of hours in the day
        :return: If not positive it returns False, else True
        """
        if num <= 0:
            return False
        else:
            self.Day = num
            return True

    def setyear(self, num):
        """
        Sets the system's standard year in system days to standardize the year across the system
        :param num: The number of days in a system year
        :return: if the Value is negative return False, else True
        """
        if num < 0:
            return False
        else:
            self.Year = num
            return True

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
        if body.Name == '':
            return False
        if body.Name in self.getnames():
            return False
        if self.Bods is None:
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
        """
        Sets the name of the system
        :param name: The name to change our system to.
        :return: Nothing
        """
        self.Name = name
        return

    def setcurrent(self, name):
        """
        Finds and sets the Current pointer to a body
        :param name: The body we are looking for
        :return: Nothing
        """
        if self.Bods is None:
            return
        self.Current = self.Bods.findbody(name)
        if self.Current.Name != name:
            print('There\'s been a problem finding it, but something return anyway.')
        return

    def deletebody(self, body):
        """
        Routes to the delete function of the body given.
        :param body: the body we are going to delete.
        :return: Returns the parent of the deleted body or nothing.
        """
        if body.Parent:
            return body.Parent.deletechild(body)
        else:
            self.Bods = None
            self.Current = None
            return None

    def orbitdistance(self, name=None):
        """
        Orbit distance getter, specifically for a body to it's parent
        :param name: The name of the body we want to find, if empty, goes to current
        :return: Returns the distance in AU's
        """
        if name is None:
            return self.Current.getdistance()
        else:
            temp = self.Current.findbody()
            return temp.getdistance()

    def changedistance(self, distance=1.0, name=None):
        if name is None:
            name = self.Current.Name
        temp = self.Bods.findbody(name)
        temp.setdistance(distance)
        return

    def calculatephase(self, name, target, date):
        """
        Calculates the phase of one body relative to another
        :param name: the body we are viewing from
        :param target: the body we are viewing
        :return: the degree of phase difference from direct illumination
        """
        return


class Body:
    """
    Body Class
    Holds all data for our celestial bodies.
    """
    def __init__(self, name='', year=0, day=24, offset=0, parent=None, extra=None):
        # Name of the body
        self.Name = name
        # Length of the year in hours
        self.Year = year
        # length of the day in hours
        self.Day = day
        # offset from 0 that it start around the planet
        self.Offset = offset
        # the body it orbits about.
        self.Parent = parent
        # The children of the body that orbit it.
        self.children = []
        # Extra data for the body
        if extra is None:
            if self.Parent is None:
                extra = {'Ratio': STDSOLRAT}
            else:
                extra = {'Ratio': STDTERRAT}
        self.Extra = extra

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
        return

    def getnames(self, ret):
        """
        Retrieves the names of the bodies and children of this body
        :param ret: the array to be returned
        :return: an array of names, passed back through ret.
        """
        ret.append(self.Name)
        for i in self.children:
            i.getnames(ret)

    def addbodyto(self, name, body):
        """
        Adds a body to the body if it's name matches, used in recursion
        :param name: The name to attach it to.
        :param body: The body to attach
        :return: True or false for success
        """
        if self.Name == name:
            body.Parent = self
            self.children.append(body)
            return True

        for i in self.children:
            if i.addbodyto(name, body):
                return True

        return False

    def namesindict(self, ret):
        """
        Names of the body and it's children in simplified dict form.
        :param ret: The dict to be returned
        :return: The ret, passed back through Param.
        """
        ret[self.Name] = {}
        for i in self.children:
            i.namesindict(ret[self.Name])

    def findbody(self, name):
        """
        Used to search through this body and it's children down.
        :param name: The name we are looking for
        :return: Either returns a body, either itself, one of it's children, or None if failed.
        """
        if name == self.Name:
            return self
        else:
            for i in self.children:
                temp = i.findbody(name)
                if temp is not None:
                    return temp
        return None

    def deletechild(self, body):
        """
        Deletes one of the children of the body.
        :param body: the body to be deleted.
        :return: Returns itself and if it deletes the body, else raises an exception
        """
        if body in self.children:
            self.children.remove(body)
        else:
            raise Exception
        return self

    def getdistance(self, target=None):
        """
        Gets the distance between this body and another body.
        :param target: if None, gets the distance between this body and it's parent
                       TODO else, it triangulates the distance using angles, and orbital distances
        """
        if target is None:
            if self.Parent is None:
                return 0
            target = self.Parent
            ratio = target.Extra['Ratio']
            distance = (self.Year**2/ratio)**(1/3)
            return distance
        else:
            return 0

    def getparentratio(self):
        if self.Parent is None:
            return 0
        else:
            return self.Parent.Extra['Ratio']
