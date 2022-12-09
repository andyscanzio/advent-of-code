import unittest

import day06


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
