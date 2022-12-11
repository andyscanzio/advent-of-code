from functools import reduce
from operator import mul
from typing import Callable

import utils

monkeys = utils.load_input("day11")


def parse_monkey(
    text: str,
) -> tuple[list[int], Callable[[int], int], tuple[int, int, int]]:
    items: list[int] = []
    operation: Callable[[int], int] = lambda x: x
    test: int = 1
    if_true: int = 0
    if_false: int = 0
    for line in text.split("\n"):
        if "Starting items:" in line:
            items = list(map(int, line.split(": ")[1].split(", ")))
        if "Operation:" in line:
            operation = eval("lambda old: " + line.split(" = ")[1])
        if "Test:" in line:
            test = int(line.split(" by ")[1])
        if "If true:" in line:
            if_true = int(line.split("throw to monkey ")[1])
        if "If false:" in line:
            if_false = int(line.split("throw to monkey ")[1])

    return items, operation, (test, if_true, if_false)


def parse_monkeys(
    text: str,
) -> tuple[list[list[int]], list[Callable[[int], int]], list[tuple[int, int, int]]]:
    items: list[list[int]] = []
    operations: list[Callable[[int], int]] = []
    decisions: list[tuple[int, int, int]] = []
    for monkey in text.split("\n\n"):
        item, operation, decision = parse_monkey(monkey)
        items.append(item)
        operations.append(operation)
        decisions.append(decision)
    return items, operations, decisions


def part1(text: str) -> int:
    items, operations, decisions = parse_monkeys(text)
    inspect = [0] * len(items)
    for _ in range(20):
        for monkey in range(len(items)):
            while items[monkey]:
                item = items[monkey].pop(0)
                inspect[monkey] += 1
                worry = operations[monkey](item) // 3
                if worry % decisions[monkey][0] == 0:
                    to_monkey = decisions[monkey][1]
                else:
                    to_monkey = decisions[monkey][2]
                items[to_monkey].append(worry)
    ans = sorted(inspect, reverse=True)
    return ans[0] * ans[1]


def part2(text: str) -> int:
    items, operations, decisions = parse_monkeys(text)
    common = reduce(mul, [decision[0] for decision in decisions])
    inspect = [0] * len(items)
    for _ in range(10000):
        for monkey in range(len(items)):
            while items[monkey]:
                item = items[monkey].pop(0) % common
                inspect[monkey] += 1
                worry = operations[monkey](item) % common
                if worry % decisions[monkey][0] == 0:
                    to_monkey = decisions[monkey][1]
                else:
                    to_monkey = decisions[monkey][2]
                items[to_monkey].append(worry)
    ans = sorted(inspect, reverse=True)
    return ans[0] * ans[1]


if __name__ == "__main__":
    print(part1(monkeys))
    print(part2(monkeys))
