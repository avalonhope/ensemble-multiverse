from evennia.utils.test_resources import EvenniaTest
from worlds.skills import proficiency


class TestSkills(EvenniaTest):
    def test_level1_proficiency(self):
        self.assertEqual(proficiency(0), 1.0)

    def test_level2_proficiency(self):
        self.assertEqual(proficiency(1000), 2.0)

    def test_level3_proficiency(self):
        self.assertEqual(proficiency(8000), 3.0)

    def test_negative_experience(self):
        self.assertEqual(proficiency(-1), 1.0)
