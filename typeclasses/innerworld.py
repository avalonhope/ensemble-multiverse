"""
Inner Worlds
Inner Worlds exist within characters that are Plural Systems.
"""
from evennia import DefaultRoom
from typeclasses.rooms import Location  # type: ignore


class Home(DefaultRoom):
    """
    Home location for arriving at an inner world.
    """

    def at_object_creation(self):
        self.db.level = Location.UNIVERSE
