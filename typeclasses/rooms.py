"""
Room

Rooms are simple containers that have no sub-locations.

"""

from enum import IntEnum
from evennia import DefaultRoom


class Location(IntEnum):
    """
    Each level is contained with the next level up,
    for example a room is inside a building.
    """

    ROOM = 0  # cannot have any sub-rooms, lowest possible level
    BUILDING = 1  # structure, cavern, vehicle, shuttle
    AREA = 2  # street, village, docking bay, open terrain
    DISTRICT = 3  # major village, town quarter, large ship
    TOWN = 4  # space station, county, shipyard, wilderness, floating city
    REGION = 5  # major city, province, duchy, atmospheric layer
    COUNTRY = 6  # major country or minor planet, atmosphere of major planet, moon
    PLANET = 7  # planets, stars, inner worlds for most species
    SYSTEM = 8  # single star system
    SECTOR = 9  # large group of star systems
    GALAXY = 10  # single galaxy, inner world for some species
    CLUSTER = 11  # galaxy cluster or group
    SUPERCLUSTER = 12  # any large cosmic structure
    UNIVERSE = 13  # physical space-time continuum, inner worlds for advanced species
    MULTIVERSE = 14  # all of creation, visible and invisible, highest possible level


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
        """Define the initial attributes of the room."""
        self.db.level = Location.ROOM
