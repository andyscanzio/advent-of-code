import utils

rocks = utils.load_input("day14")


def part1(text: str) -> int:
    walls: set[tuple[int, int]] = set()
    highest: dict[int, int] = {}
    lines = text.splitlines()
    for line in lines:
        blocks = line.split(" -> ")
        for start, end in zip(blocks[:-1], blocks[1:]):
            x1, y1 = tuple(map(int, start.split(",")))
            x2, y2 = tuple(map(int, end.split(",")))
            if x1 == x2:
                for i in range(abs(y2 - y1) + 1):
                    x, y = x1, min(y1, y2) + i
                    walls.add((x, y))
                    if x not in highest:
                        highest[x] = y
                    else:
                        highest[x] = max(y, highest[x])
            elif y1 == y2:
                for i in range(abs(x2 - x1) + 1):
                    x, y = min(x1, x2) + i, y1
                    walls.add((x, y))
                    if x not in highest:
                        highest[x] = y
                    else:
                        highest[x] = max(y, highest[x])
    unit = 0
    while True:
        unit += 1
        x, y = 500, 0
        while True:
            if x not in highest:
                break
            elif highest[x] < y:
                break
            if (x, y + 1) not in walls:
                y += 1
            elif (x - 1, y + 1) not in walls:
                x, y = x - 1, y + 1
            elif (x + 1, y + 1) not in walls:
                x, y = x + 1, y + 1
            else:
                walls.add((x, y))
                break

        if x not in highest:
            break
        elif highest[x] < y:
            break
    return unit - 1


def part2(text: str) -> int:
    walls: set[tuple[int, int]] = set()
    highest: dict[int, int] = {}
    lines = text.splitlines()
    for line in lines:
        blocks = line.split(" -> ")
        for start, end in zip(blocks[:-1], blocks[1:]):
            x1, y1 = tuple(map(int, start.split(",")))
            x2, y2 = tuple(map(int, end.split(",")))
            if x1 == x2:
                for i in range(abs(y2 - y1) + 1):
                    x, y = x1, min(y1, y2) + i
                    walls.add((x, y))
                    if x not in highest:
                        highest[x] = y
                    else:
                        highest[x] = max(y, highest[x])
            elif y1 == y2:
                for i in range(abs(x2 - x1) + 1):
                    x, y = min(x1, x2) + i, y1
                    walls.add((x, y))
                    if x not in highest:
                        highest[x] = y
                    else:
                        highest[x] = max(y, highest[x])
    floor = max(highest.values()) + 2

    unit = 0
    while True:
        unit += 1
        x, y = 500, 0
        if (x, y) in walls:
            break
        while True:
            if (x, y + 1) not in walls and y + 1 != floor:
                y += 1
            elif (x - 1, y + 1) not in walls and y + 1 != floor:
                x, y = x - 1, y + 1
            elif (x + 1, y + 1) not in walls and y + 1 != floor:
                x, y = x + 1, y + 1
            else:
                walls.add((x, y))
                break
    return unit - 1


if __name__ == "__main__":
    print(part1(rocks))
    print(part2(rocks))
