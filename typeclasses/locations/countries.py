"""
Country
Countries are simple containers located within a Planet.
"""

from typeclasses.locations import Location
from world.logic.location_types import LocationType  # type: ignore


class Country(Location):
    """Countries may contain RegionObjects and CityObjects."""

    def at_object_creation(self):
        self.db.level = LocationType.COUNTRY
