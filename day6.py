import aoc

packets = aoc.load_input("day06")


def part1(text: str) -> int:
    for i in range(len(text) - 4):
        if len(set(text[i : i + 4])) == 4:
            return i + 4
    return 0


def part2(text: str) -> int:
    for i in range(len(text) - 14):
        if len(set(text[i : i + 14])) == 14:
            return i + 14
    return 0


if __name__ == "__main__":
    print(part1(packets))
    print(part2(packets))
