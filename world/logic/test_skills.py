import unittest
from hypothesis import given
from hypothesis.strategies import integers
from world.logic.skills import proficiency  # type: ignore


class TestSkills(unittest.TestCase):
    """Test skills system."""

    @given(integers())
    def test_proficiency_min_value(self, x):
        """Test minimum value of result."""
        self.assertGreaterEqual(proficiency(x), 1.0)

    @given(integers(), integers())
    def test_proficiency_increasing_with_experience(self, x, y):
        """Verify that result is strictly increasing."""
        if 0 <= x < y:
            self.assertGreaterEqual(proficiency(y), proficiency(x))
        if x > y >= 0:
            self.assertGreaterEqual(proficiency(x), proficiency(y))
        if x == y:
            self.assertEqual(proficiency(y), proficiency(x))

    @given(integers())
    def test_inverse_proficiency(self, x):
        """Test that the result is the correct value."""
        skill_level = proficiency(x)
        if x > 0:
            y = round((((skill_level - 1.0) * 10) ** 3), 1)
            if x != y:
                self.assertEqual(proficiency(x), proficiency(y))
        else:
            self.assertEqual(skill_level, 1.0)

    def test_proficiency(self):
        """Test skill level calculation."""
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
