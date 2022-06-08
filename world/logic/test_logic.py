import unittest
from world.logic.system import System as LogicSystem  # type: ignore


class TestLogic(unittest.TestCase):
    """Test Workflow and Business Logic."""

    def test_sanity_check(self):
        """Test System Integrity."""
        system = LogicSystem()
        self.assertTrue(system.active())
