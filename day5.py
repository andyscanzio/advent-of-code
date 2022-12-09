import itertools

import aoc

instructions = aoc.load_input("day05")


def get_end_stacks(text: str) -> int:
    for i, line in enumerate(text.split("\n")):
        if "1" in line:
            return i
    return 0


def get_stacks(text_list: list[str]) -> list[list[str]]:
    stacks: list[list[str]] = []
    for line in itertools.zip_longest(*text_list, fillvalue=" "):
        if any(map(lambda x: x.isalpha(), line)):
            stacks.append([i for i in reversed(line) if i.isalpha()])
    return stacks


def move_box(stacks: list[list[str]], move: str) -> None:
    n, fr, to = map(int, move.split(" ")[1::2])
    for _ in range(n):
        stacks[to - 1].append(stacks[fr - 1].pop())


def move_boxes(stacks: list[list[str]], move: str) -> None:
    n, fr, to = map(int, move.split(" ")[1::2])
    temp: list[str] = []
    for _ in range(n):
        temp.insert(0, stacks[fr - 1].pop())
    stacks[to - 1].extend(temp)


def part1(text: str) -> str:
    stack_list = text.split("\n")[: get_end_stacks(text)]
    moves = text.split("\n")[get_end_stacks(text) + 2 :]
    stacks = get_stacks(stack_list)
    for move in moves:
        move_box(stacks, move)
    return "".join(stack[-1] for stack in stacks)


def part2(text: str) -> str:
    stack_list = text.split("\n")[: get_end_stacks(text)]
    moves = text.split("\n")[get_end_stacks(text) + 2 :]
    stacks = get_stacks(stack_list)
    for move in moves:
        move_boxes(stacks, move)
    return "".join(stack[-1] for stack in stacks)


if __name__ == "__main__":
    print(part1(instructions))
    print(part2(instructions))
