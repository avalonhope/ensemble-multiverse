"""
Room

Rooms are simple containers that has no location of their own.

"""

from enum import Enum
from evennia import DefaultRoom
from commands.default_cmdsets import RoleplayingCmdset, TrainingCmdset


class Location(Enum):
    ROOM = 0
    BUILDING = 1  # structure, cavern
    AREA = 2  # street, village
    DISTRICT = 3  # major village, town quarter
    TOWN = 4  # space station, county
    REGION = 5  # city, province, duchy
    COUNTRY = 6  # major country or minor planet
    PLANET = 7
    SYSTEM = 8
    SECTOR = 9
    GALAXY = 10
    CLUSTER = 11
    SUPERCLUSTER = 12
    UNIVERSE = 13 # inner worlds
    MULTIVERSE = 14 


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
        self.db.events = []
        self.cmdset.add(RoleplayingCmdset, permanent=True)
        self.db.level = Location.ROOM

        
class TrainingRoom(Room):
    """
    This room class is used by training rooms. It makes
    the TrainingCmdset available.
    """
    def at_object_creation(self):
        "this is called during training"
        self.cmdset.add(TrainingCmdset, permanent=True)
