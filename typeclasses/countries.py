"""
Country
Countries are simple containers located within a Planet.
"""

from evennia import DefaultRoom


class Country(DefaultRoom):
    """
    Countries are like any Object, except their location 
    is within a Planet. They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)
    See examples/object.py for a list of
    properties and methods available on all Objects.
    """

    def at_object_creation(self):
        self.db.level = Location.COUNTRY
