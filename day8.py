import aoc

trees = aoc.load_input("day8")


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


def part1(text: str) -> int:
    trees = [[int(tree) for tree in tree_line] for tree_line in text.split("\n")]
    return sum(
        is_visible(i, j, trees) for i in range(len(trees)) for j in range(len(trees[0]))
    )


def part2(text: str) -> int:
    trees = [[int(tree) for tree in tree_line] for tree_line in text.split("\n")]
    return max(
        scenic_score(i, j, trees)
        for i in range(len(trees))
        for j in range(len(trees[0]))
    )


if __name__ == "__main__":
    print(part1(trees))
    print(part2(trees))
