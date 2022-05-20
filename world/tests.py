from evennia.utils.test_resources import EvenniaTest
from hypothesis import given
from hypothesis.strategies import integers
from world.skills import proficiency


@given(integers())
def test_proficiency_min_value(x):
    assert proficiency(x) >= 1.0
    
@given(integers(), integers())
def test_proficiency_strictly_increasing(x, y):
    if x < y and x >= 0:
        assert proficiency(x) < proficiency(y)
    elif x > y and y >= 0:
        assert proficiency(x) > proficiency(y)
    elif x == y:
        assert proficiency(x) == proficiency(y)

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
