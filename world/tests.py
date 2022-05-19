from evennia.utils.test_resources import EvenniaTest
from worlds.skills import proficiency

class TestSkills(EvenniaTest):
    def test_level1_proficiency(self):
      self.assertEqual(proficiency(0), 1.0)
      
    def test_level2_proficiency(self):
      self.assertEqual(proficiency(1000), 2.0)
