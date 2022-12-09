import unittest

import day09


class TestDay09(unittest.TestCase):
    def test_part1(self):
        text = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
        self.assertEqual(day09.part1(text), 13)

    def test_part2_v1(self):
        text = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
        self.assertEqual(day09.part2(text), 1)

    def test_part2_v2(self):
        text = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
        self.assertEqual(day09.part2(text), 36)
