from pprint import pprint


def main() -> tuple[int, int]:
    elves: list[int] = []

    with open("/Users/andyscanzio/Developer/adventofcode2022/day1/input.txt", "r") as f:
        text = f.read()
        elves = [
            sum(map(int, elf.rstrip("\n").split("\n"))) for elf in text.split("\n\n")
        ]
    return max(elves), sum(sorted(elves, reverse=True)[:3])


if __name__ == "__main__":
    sol1, sol2 = main()
    print(f"The elf carrying the most Calories is carrying {sol1} calories")
    print(
        f"The top three eleves carrying the most Calories are carrying {sol2} calories"
    )