# type: ignore
from evennia.utils.test_resources import EvenniaCommandTest

from typeclasses.characters import Character
from typeclasses.rooms import Room


class TestFactionClaim(EvenniaCommandTest):
    """Test faction claims and disputes."""

    character_typeclass = Character
    room_typeclass = Room

    def test_unclaimed_room(self):
        """Test that an unclaimed room can be claimed."""

    def test_disputed_claim(self):
        """Test dispute handling for already claimed rooms."""


class TestLocalManager(EvenniaCommandTest):
    """Test the determination of manager for a location."""
