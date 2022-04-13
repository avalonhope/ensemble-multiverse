"""
Planet
Planets are located within a Star System and may contain Countries.
"""

from evennia import DefaultRoom
from typeclasses.rooms import Location

class Planet(DefaultRoom):
    """
    Countries are like any Object, except their location 
    is within a Star System. They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)
    See examples/object.py for a list of
    properties and methods available on all Objects.
    """

    def at_object_creation(self):
        self.db.level = Location.PLANET
