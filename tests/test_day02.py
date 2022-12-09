import unittest

import day02


class TestDay02(unittest.TestCase):
    def test_part1(self):
        text = """A Y
B X
C Z"""
        self.assertEqual(day02.part1(text), 15)

    def test_part2(self):
        text = """A Y
B X
C Z"""
        self.assertEqual(day02.part2(text), 12)
