import unittest
from world.logic.system import System as LogicSystem  # type: ignore


class TestLogic(unittest.TestCase):
    """Test Workflow and Business Logic."""

    def setUp(self):
        """Set up the system under test."""
        self.system = LogicSystem()

    def test_active(self):
        """Test System Integrity."""
        self.assertTrue(self.system.active())

    def test_quests(self):
        """Test List of Quests."""
        self.assertNotNone(self.system.quests())
