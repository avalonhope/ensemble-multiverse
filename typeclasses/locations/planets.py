""" Planets are located within a Star System and may contain Countries. """

from typeclasses.locations.locations import Location
from world.logic.locations import LocationType


class Planet(Location):
    """Locations within a star system such as planets or moons."""

    def at_object_creation(self):
        self.db.locationType = LocationType.PLANET
