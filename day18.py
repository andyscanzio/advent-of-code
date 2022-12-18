import utils

cubes = utils.load_input("day18")


def part1(text: str) -> int:
    all_cubes: set[tuple[int, int, int]] = set()
    area = 0
    for line in text.splitlines():
        cube = tuple(map(int, line.split(",")))
        hidden_area = 0
        for other in all_cubes:
            if (
                (
                    abs(cube[0] - other[0]) == 1
                    and cube[1] == other[1]
                    and cube[2] == other[2]
                )
                or (
                    abs(cube[1] - other[1]) == 1
                    and cube[2] == other[2]
                    and cube[0] == other[0]
                )
                or (
                    abs(cube[2] - other[2]) == 1
                    and cube[0] == other[0]
                    and cube[1] == other[1]
                )
            ):
                hidden_area += 1
        area += 6 - 2 * hidden_area
        all_cubes.add(cube)
    return area


def get_neighbors(point: tuple[int, int, int], minv: int, maxv: int):
    candidates: set[tuple[int, int, int]] = set()
    for delta in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        new_point = tuple([d + offset for d, offset in zip(point, delta)])
        if not all([d >= minv and d <= maxv for d in new_point]):
            continue
        candidates.add(new_point)
    return candidates


def part2(text: str):
    area = 0
    puzzle = {tuple(map(int, line.split(","))) for line in text.splitlines()}
    minv = min(min(point) for point in puzzle) - 1
    maxv = max(max(point) for point in puzzle) + 1
    nodes = [(minv, minv, minv)]
    visited = {nodes[0]}
    while nodes:
        node = nodes.pop()
        for neighbor in get_neighbors(node, minv, maxv):
            if neighbor in visited:
                continue
            if neighbor in puzzle:
                area += 1
            else:
                visited.add(neighbor)
                nodes.append(neighbor)

    return area


if __name__ == "__main__":
    print(part1(cubes))
    print(part2(cubes))
