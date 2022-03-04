"""
Room

Rooms are simple containers that have no sub-locations.

"""

from enum import Enum
from evennia import DefaultRoom


class Location(Enum):
    # Each level is contained with the next level up, for example a room is inside a building
    ROOM = 0  # cannot have any sub-rooms, lowest possible level
    BUILDING = 1  # structure, cavern, vehicle, shuttle
    AREA = 2  # street, village, docking bay, open terrain
    DISTRICT = 3  # major village, town quarter, large ship
    TOWN = 4  # space station, county, shipyard, wilderness, floating city
    REGION = 5  # major city, province, duchy, atmospheric layer
    COUNTRY = 6  # major country or minor planet, atmosphere of major planet
    PLANET = 7  # inner worlds for most species
    SYSTEM = 8
    SECTOR = 9  # large group of star systems
    GALAXY = 10
    CLUSTER = 11
    SUPERCLUSTER = 12  # or other large cosmic structure
    UNIVERSE = 13 # inner worlds for advanced species
    MULTIVERSE = 14 # all of creation, visible and invisible, highest possible level


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    def at_object_creation(self):
        self.db.level = Location.ROOM
