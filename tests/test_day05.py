import unittest

import day05


class TestDay05(unittest.TestCase):
    def test_part1(self):
        text = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
        self.assertEqual(day05.part1(text), "CMZ")

    def test_part2(self):
        text = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
        self.assertEqual(day05.part2(text), "MCD")
