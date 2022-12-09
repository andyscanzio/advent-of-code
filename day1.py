from aoc import load_input

elves = load_input("day1")


def part1(text: str) -> int:
    elves = [sum(map(int, elf.rstrip("\n").split("\n"))) for elf in text.split("\n\n")]
    return max(elves)


def part2(text: str) -> int:
    elves = [sum(map(int, elf.rstrip("\n").split("\n"))) for elf in text.split("\n\n")]
    return sum(sorted(elves, reverse=True)[:3])


if __name__ == "__main__":
    print(part1(elves))
    print(part2(elves))
