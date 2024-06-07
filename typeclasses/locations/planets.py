"""Planets are located within a Star System and may contain Countries."""

from typeclasses.locations.locations import Location  # type: ignore
from world.logic.location_types import LocationType  # type: ignore


class Planet(Location):
    """Locations within a star system such as planets or moons."""

    def at_object_creation(self):
        """Initial properties of a planet."""
        self.db.location_type = LocationType.PLANET
        self.db.parent_type = LocationType.STAR_SYSTEM
