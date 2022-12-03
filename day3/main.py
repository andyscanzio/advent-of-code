import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


with open(os.path.join(__location__, "input.txt"), "r") as f:
    rucksack_list = f.read()


def letter(l: str) -> int:
    if l.isupper():
        return ord(l) - ord("A") + 27
    return ord(l) - ord("a") + 1


part1 = sum(
    map(
        letter,
        [
            item
            for rucksack in rucksack_list.split("\n")
            for item in set(rucksack[: len(rucksack) // 2])
            if item in set(rucksack[len(rucksack) // 2 :])
        ],
    )
)

print(part1)


part2 = sum(
    map(
        letter,
        [
            set(rucksack1)
            .intersection(set(rucksack2))
            .intersection(set(rucksack3))
            .pop()
            for rucksack1, rucksack2, rucksack3 in zip(
                *[iter(rucksack_list.split("\n"))] * 3
            )
        ],
    )
)


print(part2)
