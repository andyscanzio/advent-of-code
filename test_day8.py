import unittest

import day8


class TestDay8(unittest.TestCase):
    def test_part1(self):
        text = """30373
25512
65332
33549
35390"""
        self.assertEqual(day8.part1(text), 21)

    def test_part2(self):
        text = """30373
25512
65332
33549
35390"""
        self.assertEqual(day8.part2(text), 8)
