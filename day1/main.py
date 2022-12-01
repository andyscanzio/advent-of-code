def main() -> tuple[int, int]:
    elves: list[int] = []

    with open("/Users/andyscanzio/Developer/adventofcode2022/day1/input.txt", "r") as f:
        elf = 0
        for line in f:
            if line != "\n":
                elf += int(line)
            else:
                elves.append(elf)
                elf = 0
        elves.append(elf)

    return max(elves), sum(sorted(elves, reverse=True)[:3])


if __name__ == "__main__":
    sol1, sol2 = main()
    print(f"The elf carrying the most Calories is carrying {sol1} calories")
    print(
        f"The top three eleves carrying the most Calories are carrying {sol2} calories"
    )
