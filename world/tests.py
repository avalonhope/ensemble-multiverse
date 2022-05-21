from evennia.utils.test_resources import EvenniaTest
from hypothesis import given
from hypothesis.strategies import integers
from world.skills import proficiency


@given(integers())
def test_proficiency_min_value(x):
    """Test minimum value of result."""
    if proficiency(x) < 1.0:
        raise AssertionError


@given(integers(), integers())
def test_proficiency_strictly_increasing(x, y):
    """Verify that result is strictly increasing."""
    if 0 <= x < y and proficiency(x) >= proficiency(y):
        raise AssertionError
    if x > y >= 0 and proficiency(x) <= proficiency(y):
        raise AssertionError
    if x == y and proficiency(x) != proficiency(y):
        raise AssertionError


@given(integers())
def test_inverse_proficiency(x):
    """Test that the result is the correct value."""
    skill_level = proficiency(x)
    if x != ((skill_level - 1) * 10) ** 3:
        raise AssertionError


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
