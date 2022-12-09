import unittest

import day2


class TestDay2(unittest.TestCase):
    def test_part1(self):
        text = """A Y
B X
C Z"""
        self.assertEqual(day2.part1(text), 15)

    def test_part2(self):
        text = """A Y
B X
C Z"""
        self.assertEqual(day2.part2(text), 12)
