import os

from aoc import load_input

DEBUG = False

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

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

moves = [(line.split(" ")[0], int(line.split(" ")[1])) for line in test.split("\n")]

_input = load_input("day9")

moves = [(line.split(" ")[0], int(line.split(" ")[1])) for line in _input.split("\n")]

head = {"x": 0, "y": 0}
tail = {"x": 0, "y": 0}

spots: set[tuple[int, int]] = set()

for move in moves:
    for _ in range(move[1]):
        if move[0] == "U":
            head["y"] += 1
        if move[0] == "D":
            head["y"] -= 1
        if move[0] == "L":
            head["x"] -= 1
        if move[0] == "R":
            head["x"] += 1
        if (abs(head["x"] - tail["x"]) == 1 and abs(head["y"] - tail["y"]) > 1) or (
            abs(head["y"] - tail["y"]) == 1 and abs(head["x"] - tail["x"]) > 1
        ):
            tail["x"] += (head["x"] - tail["x"]) // abs(head["x"] - tail["x"])
            tail["y"] += (head["y"] - tail["y"]) // abs(head["y"] - tail["y"])
        if abs(head["x"] - tail["x"]) > 1:
            tail["x"] += (head["x"] - tail["x"]) // abs(head["x"] - tail["x"])
        if abs(head["y"] - tail["y"]) > 1:
            tail["y"] += (head["y"] - tail["y"]) // abs(head["y"] - tail["y"])
        spots.add((tail["x"], tail["y"]))

print(len(spots))

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


spots2: set[tuple[int, int]] = set()
if DEBUG:
    with open(os.path.join(__location__, "debug.txt"), "w") as f:
        m = [["." for _ in range(26)] for _ in range(21)]

        m[5][11] = "s"
        for i, node in enumerate(reversed(nodes)):
            j = 9 - i
            if j == 0:
                print(node)
            m[node["y"] + 5][node["x"] + 11] = str(j) if j > 0 else "H"
        with open(os.path.join(__location__, "debug.txt"), "a") as f:
            for line in reversed(m):
                f.write("".join(line))
                f.write("\n")
            f.write("\n")

for move in moves:
    if DEBUG:
        with open(os.path.join(__location__, "debug.txt"), "a") as f:
            f.write("==" + " ".join(map(str, move)) + "==")
            f.write("\n")
    for _ in range(move[1]):
        head = nodes[0]
        if move[0] == "U":
            head["y"] += 1
        elif move[0] == "D":
            head["y"] -= 1
        elif move[0] == "L":
            head["x"] -= 1
        elif move[0] == "R":
            head["x"] += 1
        for i in range(1, len(nodes)):
            tail = nodes[i]
            if (abs(head["x"] - tail["x"]) == 1 and abs(head["y"] - tail["y"]) > 1) or (
                abs(head["y"] - tail["y"]) == 1 and abs(head["x"] - tail["x"]) > 1
            ):
                tail["x"] += (head["x"] - tail["x"]) // abs(head["x"] - tail["x"])
                tail["y"] += (head["y"] - tail["y"]) // abs(head["y"] - tail["y"])
            if abs(head["x"] - tail["x"]) > 1:
                tail["x"] += (head["x"] - tail["x"]) // abs(head["x"] - tail["x"])
            if abs(head["y"] - tail["y"]) > 1:
                tail["y"] += (head["y"] - tail["y"]) // abs(head["y"] - tail["y"])
            head = tail

        spots2.add((nodes[-1]["x"], nodes[-1]["y"]))
    if DEBUG:
        m = [["." for _ in range(26)] for _ in range(21)]

        m[5][11] = "s"

        for i, node in enumerate(reversed(nodes)):
            j = 9 - i
            if j == 0:
                print(node)
            m[node["y"] + 5][node["x"] + 11] = str(j) if j > 0 else "H"
        with open(os.path.join(__location__, "debug.txt"), "a") as f:
            for line in reversed(m):
                f.write("".join(line))
                f.write("\n")
            f.write("\n")

if DEBUG:
    m = [["." for _ in range(26)] for _ in range(21)]

    for spot in spots2:
        m[spot[1] + 5][spot[0] + 11] = "#"

    for line in reversed(m):
        print("".join(line))

print(len(spots2))
