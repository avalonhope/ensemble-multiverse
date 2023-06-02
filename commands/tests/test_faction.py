from evennia.utils.test_resources import BaseEvenniaTestCase
from typeclasses.characters import Character  # type: ignore
from typeclasses.rooms import Room  # type: ignore


class TestFactionClaim(BaseEvenniaCommandTest):
    """Test faction location claims."""

    character_typeclass = Character
    room_typeclass = Room

    def test_unclaimed_room(self):
        """Test that an unclaimed room can be claimed."""

    def test_disputed_claim(self):
        """Test dispute handling for already claimed rooms."""


class TestLocalManager(CommandTest):
    """Test the determination of manager for a location."""
