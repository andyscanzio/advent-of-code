from typing import Iterable, cast

import aoc

rucksacks = aoc.load_input("day3")


def letter(l: str) -> int:
    if l.isupper():
        return ord(l) - ord("A") + 27
    return ord(l) - ord("a") + 1


def part1(text: str) -> int:
    return sum(
        map(
            letter,
            [
                item
                for rucksack in text.split("\n")
                for item in set(rucksack[: len(rucksack) // 2])
                if item in set(rucksack[len(rucksack) // 2 :])
            ],
        )
    )


def part2(text: str) -> int:
    return sum(
        map(
            letter,
            [
                set(rucksack1)
                .intersection(set(rucksack2))
                .intersection(set(rucksack3))
                .pop()
                for rucksack1, rucksack2, rucksack3 in cast(
                    Iterable[tuple[str, str, str]], zip(*[iter(text.split("\n"))] * 3)
                )
            ],
        )
    )


if __name__ == "__main__":
    print(part1(rucksacks))
    print(part2(rucksacks))
