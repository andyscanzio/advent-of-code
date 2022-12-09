import aoc

strategies = aoc.load_input("day2")


def part1(text: str) -> int:
    strategies = [(line.split(" ")[0], line.split(" ")[1]) for line in text.split("\n")]
    point: dict[tuple[str, str], int] = {
        ("A", "X"): 1 + 3,
        ("A", "Y"): 2 + 6,
        ("A", "Z"): 3 + 0,
        ("B", "X"): 1 + 0,
        ("B", "Y"): 2 + 3,
        ("B", "Z"): 3 + 6,
        ("C", "X"): 1 + 6,
        ("C", "Y"): 2 + 0,
        ("C", "Z"): 3 + 3,
    }
    return sum(point[strategy] for strategy in strategies)


def part2(text: str) -> int:
    strategies = [(line.split(" ")[0], line.split(" ")[1]) for line in text.split("\n")]
    point: dict[tuple[str, str], int] = {
        ("A", "X"): 3 + 0,
        ("A", "Y"): 1 + 3,
        ("A", "Z"): 2 + 6,
        ("B", "X"): 1 + 0,
        ("B", "Y"): 2 + 3,
        ("B", "Z"): 3 + 6,
        ("C", "X"): 2 + 0,
        ("C", "Y"): 3 + 3,
        ("C", "Z"): 1 + 6,
    }
    return sum(point[strategy] for strategy in strategies)


if __name__ == "__main__":
    print(part1(strategies))
    print(part2(strategies))
