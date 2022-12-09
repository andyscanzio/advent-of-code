import unittest

import day01


class TestDay01(unittest.TestCase):
    def test_part1(self):
        text = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
        self.assertEqual(day01.part1(text), 24000)

    def test_part2(self):
        text = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
        self.assertEqual(day01.part2(text), 45000)
