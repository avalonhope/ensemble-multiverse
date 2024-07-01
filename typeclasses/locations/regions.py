"""Regions within a Country."""

from typeclasses.locations.locations import Location  # type: ignore
from world.logic.location_types import LocationType  # type: ignore


class Region(Location):
    """Region within a Country."""

    def at_object_creation(self):
        """Initial properties of a region."""
        self.db.location_type = LocationType.REGION
        self.db.parent_type = LocationType.COUNTRY
