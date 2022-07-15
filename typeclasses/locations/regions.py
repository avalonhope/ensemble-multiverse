"""
Region
Regions are locations within a Country location
"""

from typeclasses.locations.locations import Location
from world.logic.locations import LocationType


class Region(Location):
    """
    Regions are like any Object, except their location is within a Country.
    They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)
    See examples/object.py for a list of
    properties and methods available on all Objects.
    """

    def at_object_creation(self):
        self.db.location_type = LocationType.REGION
