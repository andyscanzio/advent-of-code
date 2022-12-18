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
import day11
import day12
import day13
import day14
import day15
import day16


class TestDay01(unittest.TestCase):
    def setUp(self):
        self.text = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

    def test_part1(self):
        self.assertEqual(day01.part1(self.text), 24000)

    def test_part2(self):
        self.assertEqual(day01.part2(self.text), 45000)


class TestDay02(unittest.TestCase):
    def setUp(self):
        self.text = """A Y
B X
C Z"""

    def test_part1(self):
        self.assertEqual(day02.part1(self.text), 15)

    def test_part2(self):
        self.assertEqual(day02.part2(self.text), 12)


class TestDay03(unittest.TestCase):
    def setUp(self):
        self.text = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    def test_part1(self):
        self.assertEqual(day03.part1(self.text), 157)

    def test_part2(self):
        self.assertEqual(day03.part2(self.text), 70)


class TestDay04(unittest.TestCase):
    def setUp(self):
        self.text = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    def test_part1(self):
        self.assertEqual(day04.part1(self.text), 2)

    def test_part2(self):
        self.assertEqual(day04.part2(self.text), 4)


class TestDay05(unittest.TestCase):
    def setUp(self):
        self.text = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    def test_part1(self):
        self.assertEqual(day05.part1(self.text), "CMZ")

    def test_part2(self):
        self.assertEqual(day05.part2(self.text), "MCD")


class TestDay06(unittest.TestCase):
    def setUp(self):
        self.text_part1_list = [
            "bvwbjplbgvbhsrlpgdmjqwftvncz",
            "nppdvjthqldpwncqszvftbrmjlhg",
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
        ]
        self.text_part2_list = [
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
            "bvwbjplbgvbhsrlpgdmjqwftvncz",
            "nppdvjthqldpwncqszvftbrmjlhg",
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
        ]
        self.result_part1_list = [5, 6, 10, 11]
        self.result_part2_list = [19, 23, 23, 29, 26]

    def test_part1(self):
        for text, result in zip(self.text_part1_list, self.result_part1_list):
            self.assertEqual(day06.part1(text), result)

    def test_part2(self):
        for text, result in zip(self.text_part2_list, self.result_part2_list):
            self.assertEqual(day06.part2(text), result)


class TestDay07(unittest.TestCase):
    def setUp(self):
        self.text = """$ cd /
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

    def test_part1(self):
        self.assertEqual(day07.part1(self.text), 95437)

    def test_part2(self):
        self.assertEqual(day07.part2(self.text), 24933642)


class TestDay08(unittest.TestCase):
    def setUp(self):
        self.text = """30373
25512
65332
33549
35390"""

    def test_part1(self):
        self.assertEqual(day08.part1(self.text), 21)

    def test_part2(self):
        self.assertEqual(day08.part2(self.text), 8)


class TestDay09(unittest.TestCase):
    def setUp(self):
        self.text_v1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
        self.text_v2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

    def test_part1(self):
        self.assertEqual(day09.part1(self.text_v1), 13)

    def test_part2_v1(self):
        self.assertEqual(day09.part2(self.text_v1), 1)

    def test_part2_v2(self):
        self.assertEqual(day09.part2(self.text_v2), 36)


class TestDay10(unittest.TestCase):
    def setUp(self):
        self.text = """addx 15
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

    def test_part1(self):
        self.assertEqual(day10.part1(self.text), 13140)

    def test_part2(self):
        self.assertEqual(
            day10.part2(self.text),
            """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....""",
        )


class TestDay11(unittest.TestCase):
    def setUp(self):
        self.monkey = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3"""

        self.text = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

    def test_parse_monkey(self):
        items, operation, decision = day11.parse_monkey(self.monkey)
        self.assertEqual(items, [79, 98])
        self.assertEqual(list(map(operation, items)), [1501, 1862])
        self.assertEqual(decision, (23, 2, 3))

    def test_part1(self):
        self.assertEqual(day11.part1(self.text), 10605)

    def test_part2(self):
        self.assertEqual(day11.part2(self.text), 2713310158)


class TestDay12(unittest.TestCase):
    def setUp(self):
        self.text = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

    def test_part1(self):
        self.assertEqual(day12.part1(self.text), 31)

    def test_part2(self):
        self.assertEqual(day12.part2(self.text), 29)


class TestDay13(unittest.TestCase):
    def setUp(self):
        self.test_inputs = [  # type: ignore
            ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]),
            ([[1], [2, 3, 4]], [[1], 4]),
            ([9], [[8, 7, 6]]),
            ([[4, 4], 4, 4], [[4, 4], 4, 4, 4]),
            ([7, 7, 7, 7], [7, 7, 7]),
            ([], [3]),
            ([[[]]], [[]]),
            ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]),
        ]
        self.results = [True, True, False, True, False, True, False, False]
        self.text = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

    def test_compare(self):
        for (left, right), result in zip(self.test_inputs, self.results):  # type: ignore
            self.assertEqual(day13.compare(left, right), result)  # type: ignore

    def test_part1(self):
        self.assertEqual(day13.part1(self.text), 13)

    def test_part2(self):
        self.assertEqual(day13.part2(self.text), 140)


class TestDay14(unittest.TestCase):
    def setUp(self):
        self.text = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

    def test_part1(self):
        self.assertEqual(day14.part1(self.text), 24)

    def test_part2(self):
        self.assertEqual(day14.part2(self.text), 93)


class TestDay15(unittest.TestCase):
    def setUp(self):
        self.text = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
        self.row = 10
        self.size = 20

    def test_part1(self):
        self.assertEqual(day15.part1(self.text, self.row), 26)

    def test_part2(self):
        self.assertEqual(day15.part2(self.text, self.size), 56000011)


class TestDay16(unittest.TestCase):
    def setUp(self):
        self.text = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

    def test_part1(self):
        self.assertEqual(day16.part1(self.text), 1651)

    def test_part2(self):
        self.assertEqual(day16.part2(self.text), 1707)
