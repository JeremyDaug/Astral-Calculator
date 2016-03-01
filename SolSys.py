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
        self.Name = "Unnamed"
        self._Heart = None  # Points to a body that will be treated as the Central most body (Such as the star)
        self._Special = {}  # A dict of special traits, if empty assume heliocentric with no peculiarities


class Body:
    def __init__(self):
        self._Name = 'NA'  # The name of the body, should be unique, but is not required.
        self._Day = 24  # The length of the body's day in hours.
        self._Year = 0  # The length of the year in the body's day
        self._Start = 0  # The offset from 0 in degrees the body starts at
        self._Solstice = 0  # The day of the year that is counted as winter
        self._Special = {}  # A place holder Dict for oddity data, such as 90 Deg tilted planets and the like.
        self._Parent = None  # Points to the body it orbits, if empty it's the central planet
        self._Kids = None  # A list of bodies that orbit the body
