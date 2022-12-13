import ast
from functools import cmp_to_key
from typing import Any

import utils

packets = utils.load_input("day13")


def compare(left: list[Any], right: list[Any]) -> bool | None:
    for l, r in zip(left, right):
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return True
            elif l > r:
                return False
        elif isinstance(l, list) and isinstance(r, list):
            temp = compare(l, r)  # type: ignore
            if temp is not None:
                return temp
        elif isinstance(l, int) and isinstance(r, list):
            temp = compare([l], r)  # type: ignore
            if temp is not None:
                return temp
        elif isinstance(l, list) and isinstance(r, int):
            temp = compare(l, [r])  # type: ignore
            if temp is not None:
                return temp

    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False


def part1(text: str) -> int:
    packets = text.split("\n\n")
    return sum(
        idx + 1
        for idx, packet in enumerate(packets)
        if compare(
            ast.literal_eval(packet.splitlines()[0]),
            ast.literal_eval(packet.splitlines()[1]),
        )
    )


def sort_compare(left: list[Any], right: list[Any]) -> int:
    temp = compare(left, right)
    if temp:
        return -1
    return 1


def part2(text: str) -> int:
    packets = text.split("\n\n")
    left = [ast.literal_eval(packet.splitlines()[0]) for packet in packets]
    right = [ast.literal_eval(packet.splitlines()[1]) for packet in packets]
    full = left + right + [[[2]]] + [[[6]]]
    full_sorted = sorted(full, key=cmp_to_key(sort_compare))
    return (full_sorted.index([[2]]) + 1) * (full_sorted.index([[6]]) + 1)


if __name__ == "__main__":
    print(part1(packets))
    print(part2(packets))
