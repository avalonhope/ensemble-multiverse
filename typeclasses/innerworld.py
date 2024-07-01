"""
Inner Worlds
Inner Worlds exist within all Sentient Beings, but not all are aware of this.
"""

from evennia import DefaultRoom
from typeclasses.rooms import Location  # type: ignore


class Home(DefaultRoom):
    """Home location for arriving at an inner world."""

    def at_object_creation(self):
        """The inner world is like a small universe."""
        self.db.level = Location.UNIVERSE
