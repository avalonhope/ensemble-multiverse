from evennia.utils.test_resources import EvenniaTest
from world.skills import proficiency

class TestSkills(EvenniaTest):
    def test_proficiency(self):
        expected = {
          0: 1.0,
          1000: 2.0,
          8000: 3.0,
          27000: 4.0,
          64000: 5.0,
        }
        for value in expected:
          self.assertEqual(proficency(value), expected(value))
