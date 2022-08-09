"""
Country
Countries are simple containers located within a Planet.
"""

from typeclasses.locations.locations import Location  # type: ignore
from world.logic.location_types import LocationType  # type: ignore


class Country(Location):
    """Countries may contain RegionObjects and CityObjects."""

    def at_object_creation(self):
        """When a country location is created."""
        self.db.level = LocationType.COUNTRY
