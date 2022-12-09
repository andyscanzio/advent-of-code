import unittest

import day4


class TestDay4(unittest.TestCase):
    def test_part1(self):
        text = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
        self.assertEqual(day4.part1(text), 2)

    def test_part2(self):
        text = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
        self.assertEqual(day4.part2(text), 4)
