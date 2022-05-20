from evennia.utils.test_resources import EvenniaTest
from world.skills import proficiency


class TestSkills(EvenniaTest):
    """Test skills system."""

    def test_proficiency(self):
        """"Test skill level calculation."""
        examples = {
            -1: 1.0,
            0: 1.0,
            1000: 2.0,
            8000: 3.0,
            27000: 4.0,
            64000: 5.0,
            125000: 6.0,
        }
        for experience, level in examples.items():
            self.assertEqual(proficiency(experience), level)
