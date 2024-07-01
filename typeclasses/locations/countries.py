"""Country within a Planet."""

from typeclasses.locations.locations import Location  # type: ignore
from world.logic.location_types import LocationType  # type: ignore


class Country(Location):
    """Country."""

    def at_object_creation(self):
        """When a country location is created."""
        self.db.location_type = LocationType.COUNTRY
        self.db.parent_type = LocationType.PLANET
