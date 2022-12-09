import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

test = """30373
25512
65332
33549
35390"""

trees = [[int(tree) for tree in tree_line] for tree_line in test.split("\n")]

with open(os.path.join(__location__, "input.txt"), "r") as f:
    inp = f.read()

trees = [[int(tree) for tree in tree_line] for tree_line in inp.split("\n")]


def is_visible(i: int, j: int, grid: list[list[int]]) -> bool:
    if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
        return True
    tree = grid[i][j]
    row = grid[i]
    left, right = row[:j], row[j + 1 :]
    col = [grid[x][j] for x in range(len(grid))]
    top, bottom = col[:i], col[i + 1 :]

    return tree > min(
        max(left, default=0),
        max(right, default=0),
        max(top, default=0),
        max(bottom, default=0),
    )


print(
    sum(
        is_visible(i, j, trees) for i in range(len(trees)) for j in range(len(trees[0]))
    )
)


def scenic_score(i: int, j: int, grid: list[list[int]]) -> int:
    tree = grid[i][j]
    row = grid[i]
    left, right = row[:j][::-1], row[j + 1 :]
    col = [grid[x][j] for x in range(len(grid))]
    top, bottom = col[:i][::-1], col[i + 1 :]
    l = 0
    for q in left:
        l += 1
        if q >= tree:
            break
    r = 0
    for q in right:
        r += 1
        if q >= tree:
            break
    t = 0
    for q in top:
        t += 1
        if q >= tree:
            break
    b = 0
    for q in bottom:
        b += 1
        if q >= tree:
            break
    return l * r * t * b


print(
    max(
        scenic_score(i, j, trees)
        for i in range(len(trees))
        for j in range(len(trees[0]))
    )
)


def part1(text: str) -> int:
    return 1


def part2(text: str) -> int:
    return 2
