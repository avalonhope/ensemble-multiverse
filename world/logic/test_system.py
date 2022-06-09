import unittest
from world.logic.system import System as LogicSystem  # type: ignore


class TestLogic(unittest.TestCase):
    """Test Workflow and Business Logic."""

    def test_active(self):
        """Test System Integrity."""
        system = LogicSystem()
        self.assertTrue(system.active())

    def test_quests(self):
        """Test List of Quests."""
