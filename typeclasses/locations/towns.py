"""Towns"""
import icontract

from typeclasses.locations import Location
from world.logic.locations import LocationType

@icontract.invariant(lambda self: self.locationType == LocationType.TOWN)
class Town(Location):
    """Towns may contain Building and Vehicle objects."""

    def at_object_creation(self):
        self.db.locationType = LocationType.TOWN
