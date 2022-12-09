import aoc

test = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

test = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


moves = aoc.load_input("day9")


def move_head(move: str, head: dict[str, int]) -> dict[str, int]:
    x, y = head["x"], head["y"]
    if move == "U":
        y = head["y"] + 1
    if move == "D":
        y = head["y"] - 1
    if move == "L":
        x = head["x"] - 1
    if move == "R":
        x = head["x"] + 1
    return {"x": x, "y": y}


def move_tail(head: dict[str, int], tail: dict[str, int]) -> dict[str, int]:
    x, y = tail["x"], tail["y"]
    if (abs(head["x"] - tail["x"]) == 1 and abs(head["y"] - tail["y"]) > 1) or (
        abs(head["y"] - tail["y"]) == 1 and abs(head["x"] - tail["x"]) > 1
    ):
        x = tail["x"] + (head["x"] - tail["x"]) // abs(head["x"] - tail["x"])
        y = tail["y"] + (head["y"] - tail["y"]) // abs(head["y"] - tail["y"])
    if abs(head["x"] - tail["x"]) > 1:
        x = tail["x"] + (head["x"] - tail["x"]) // abs(head["x"] - tail["x"])
    if abs(head["y"] - tail["y"]) > 1:
        y = tail["y"] + (head["y"] - tail["y"]) // abs(head["y"] - tail["y"])
    return {"x": x, "y": y}


def part1(text: str) -> int:
    moves = [(line.split(" ")[0], int(line.split(" ")[1])) for line in text.split("\n")]
    head = {"x": 0, "y": 0}
    tail = {"x": 0, "y": 0}

    spots: set[tuple[int, int]] = set()

    for move in moves:
        for _ in range(move[1]):
            head = move_head(move[0], head)
            tail = move_tail(head, tail)
            spots.add((tail["x"], tail["y"]))

    return len(spots)


def part2(text: str) -> int:

    moves = [(line.split(" ")[0], int(line.split(" ")[1])) for line in text.split("\n")]
    nodes = [
        {"x": 0, "y": 0},
        {"x": 0, "y": 0},
        {"x": 0, "y": 0},
        {"x": 0, "y": 0},
        {"x": 0, "y": 0},
        {"x": 0, "y": 0},
        {"x": 0, "y": 0},
        {"x": 0, "y": 0},
        {"x": 0, "y": 0},
        {"x": 0, "y": 0},
    ]

    spots: set[tuple[int, int]] = set()

    for move in moves:
        for _ in range(move[1]):
            nodes[0] = move_head(move[0], nodes[0])
            head = nodes[0]
            for i in range(1, len(nodes)):
                nodes[i] = move_tail(head, nodes[i])
                head = nodes[i]

            spots.add((nodes[-1]["x"], nodes[-1]["y"]))

    return len(spots)


if __name__ == "__main__":
    print(part1(moves))
    print(part2(moves))
