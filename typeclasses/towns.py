"""
Towns
"""

from evennia import DefaultRoom
from typing import Any
from world.logic.locations import Location  # type: ignore


class Town(DefaultRoom):
    """
    Towns may contain Building and Vehicle objects.
    """

    def at_object_creation(self):
        self.db.level = Location.TOWN
