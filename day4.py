import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


with open(os.path.join(__location__, "input.txt"), "r") as f:
    assignments = f.read()


assignments = [
    tuple(
        (int(elf.split("-")[0]), int(elf.split("-")[-1]))
        for elf in assignment.split(",")
    )
    for assignment in assignments.split("\n")
]


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


print(sum(overlap_completely(assignment) for assignment in assignments))

print(sum(overlap_partially(assignment) for assignment in assignments))
