import unittest

import day1
import day3


class TestDay1(unittest.TestCase):
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
        self.assertEqual(day1.part1(text), 24000)

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
        self.assertEqual(day1.part2(text), 45000)


class TestDay3(unittest.TestCase):
    def test_part1(self):
        text = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
        self.assertEqual(day3.part1(text), 157)

    def test_part2(self):
        text = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw0"""
        self.assertEqual(day3.part2(text), 70)
