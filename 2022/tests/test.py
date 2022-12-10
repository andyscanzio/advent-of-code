import unittest

import day01
import day02
import day03
import day04
import day05
import day06
import day07
import day08
import day09
import day10


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


class TestDay03(unittest.TestCase):
    def test_part1(self):
        text = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
        self.assertEqual(day03.part1(text), 157)

    def test_part2(self):
        text = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw0"""
        self.assertEqual(day03.part2(text), 70)


class TestDay04(unittest.TestCase):
    def test_part1(self):
        text = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
        self.assertEqual(day04.part1(text), 2)

    def test_part2(self):
        text = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
        self.assertEqual(day04.part2(text), 4)


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


class TestDay06(unittest.TestCase):
    def test_part1(self):
        text_list = [
            "bvwbjplbgvbhsrlpgdmjqwftvncz",
            "nppdvjthqldpwncqszvftbrmjlhg",
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
        ]
        result_list = [5, 6, 10, 11]
        for text, result in zip(text_list, result_list):
            self.assertEqual(day06.part1(text), result)

    def test_part2(self):
        text_list = [
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
            "bvwbjplbgvbhsrlpgdmjqwftvncz",
            "nppdvjthqldpwncqszvftbrmjlhg",
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
        ]
        result_list = [19, 23, 23, 29, 26]
        for text, result in zip(text_list, result_list):
            self.assertEqual(day06.part2(text), result)


class TestDay07(unittest.TestCase):
    def test_part1(self):
        text = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
        self.assertEqual(day07.part1(text), 95437)

    def test_part2(self):
        text = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
        self.assertEqual(day07.part2(text), 24933642)


class TestDay08(unittest.TestCase):
    def test_part1(self):
        text = """30373
25512
65332
33549
35390"""
        self.assertEqual(day08.part1(text), 21)

    def test_part2(self):
        text = """30373
25512
65332
33549
35390"""
        self.assertEqual(day08.part2(text), 8)


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


class TestDay10(unittest.TestCase):
    def test_part1(self):
        text = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
        self.assertEqual(day10.part1(text), 13140)

    def test_part2(self):
        text = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
        self.assertEqual(
            day10.part2(text),
            """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....""",
        )
