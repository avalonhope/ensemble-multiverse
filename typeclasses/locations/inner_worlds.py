"""Inner Worlds exist within the souls of characters."""
from typeclasses.locations.locations import Location
from world.logic.location_types import LocationType


class InnerWorld(Location):
    """An inner world exists within the soul of a character."""

    def at_object_creation(self):
        self.db.locationType = LocationType.UNIVERSE
