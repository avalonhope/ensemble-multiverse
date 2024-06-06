"""Inner Worlds exist within the souls of characters."""

from typeclasses.locations.locations import Location  # type: ignore
from world.logic.location_types import LocationType  # type: ignore


class InnerWorld(Location):
    """An inner world exists within the soul of a character."""

    def at_object_creation(self):
        """Initial properties of an Inner World."""
        self.db.locationType = LocationType.UNIVERSE
