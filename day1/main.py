import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def main() -> tuple[int, int]:
    elves: list[int] = []

    with open(os.path.join(__location__, "input.txt"), "r") as f:
        text = f.read()
        elves = [
            sum(map(int, elf.rstrip("\n").split("\n"))) for elf in text.split("\n\n")
        ]
    return max(elves), sum(sorted(elves, reverse=True)[:3])


if __name__ == "__main__":
    part1, part2 = main()
    print(f"The elf carrying the most Calories is carrying {part1} calories")
    print(
        f"The top three eleves carrying the most Calories are carrying {part2} calories"
    )
