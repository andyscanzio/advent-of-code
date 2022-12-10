import utils

assignments = utils.load_input("day04")


def overlap_completely(assignnment: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    first_elf, second_elf = assignnment
    first_elf_left, first_elf_right = first_elf
    second_elf_left, second_elf_right = second_elf
    return (
        first_elf_left <= second_elf_left <= second_elf_right <= first_elf_right
        or second_elf_left <= first_elf_left <= first_elf_right <= second_elf_right
    )


def overlap_partially(assignnment: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    first_elf, second_elf = assignnment
    first_elf_left, first_elf_right = first_elf
    second_elf_left, second_elf_right = second_elf
    return (
        first_elf_left <= second_elf_left <= first_elf_right
        or first_elf_left <= second_elf_right <= first_elf_right
        or second_elf_left <= first_elf_left <= second_elf_right
        or second_elf_left <= first_elf_right <= second_elf_right
    )


def part1(text: str) -> int:
    assignments = [
        tuple(
            (int(elf.split("-")[0]), int(elf.split("-")[-1]))
            for elf in assignment.split(",")
        )
        for assignment in text.split("\n")
    ]
    return sum(overlap_completely(assignment) for assignment in assignments)


def part2(text: str) -> int:
    assignments = [
        tuple(
            (int(elf.split("-")[0]), int(elf.split("-")[-1]))
            for elf in assignment.split(",")
        )
        for assignment in text.split("\n")
    ]
    return sum(overlap_partially(assignment) for assignment in assignments)


if __name__ == "__main__":
    print(part1(assignments))
    print(part2(assignments))
