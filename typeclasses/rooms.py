"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from commands.default_cmdsets import TrainingCmdset


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    self.db.events = []
    self.cmdset.add(RoleplayingCmdset, permanent=True)

        
class TrainingRoom(Room):
    """
    This room class is used by training rooms. It makes
    the TrainingCmdset available.
    """
    def at_object_creation(self):
        "this is called during training"
        self.cmdset.add(TrainingCmdset, permanent=True)
