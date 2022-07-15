"""Towns"""
import icontract

from evennia import DefaultExit
from typeclasses.locations import Location
from world.logic.locations import LocationType


@icontract.invariant(lambda self: self.locationType == LocationType.TOWN)
class Town(Location):
    """Towns."""

    def at_object_creation(self):
        self.db.locationType = LocationType.TOWN
        
class Road(DefaultExit):
    """Roads are the connectors for travel between Towns."""
