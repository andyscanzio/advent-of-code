import utils

elevation = utils.load_input("day12")


def create_grid(
    text: str,
) -> tuple[
    dict[tuple[int, int], int],
    dict[tuple[int, int], list[tuple[int, int]]],
    tuple[int, int],
    tuple[int, int],
]:
    lines = text.splitlines()
    start = (0, 0)
    end = (0, 0)
    grid: dict[tuple[int, int], int] = {}
    for y, line in enumerate(lines):
        for x, spot in enumerate(line):
            if spot == "S":
                start = (x, y)
                grid[(x, y)] = 0
            elif spot == "E":
                end = (x, y)
                grid[(x, y)] = 25
            else:
                grid[(x, y)] = ord(spot) - ord("a")
    neighbours: dict[tuple[int, int], list[tuple[int, int]]] = {}
    for spot in grid:
        x, y = spot
        temp = [
            (x + x_off, y + y_off)
            for x_off, y_off in ((0, -1), (-1, 0), (0, 1), (1, 0))
            if (n := (x + x_off, y + y_off)) in grid and (grid[n] - grid[spot] <= 1)
        ]
        neighbours[spot] = temp
    return grid, neighbours, start, end


def dijkstra(
    neighbours: dict[tuple[int, int], list[tuple[int, int]]],
    end: tuple[int, int],
    start: tuple[int, int] | list[tuple[int, int]],
) -> int:
    queue = list(neighbours.keys())
    n = len(queue)
    dist = {node: n for node in queue}
    prev: dict[tuple[int, int], tuple[int, int]] = {node: (-1, -1) for node in queue}
    if isinstance(start, list):
        for point in start:
            dist[point] = 0
    else:
        dist[start] = 0
    while queue:
        queue.sort(key=dist.__getitem__, reverse=True)
        u = queue.pop()
        for v in neighbours[u]:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    path = 0
    cur = end
    while prev[cur] != (-1, -1):
        path += 1
        cur = prev[cur]
    return path


def part1(text: str) -> int:
    _, neighbours, start, end = create_grid(text)
    return dijkstra(neighbours, end, start)


def part2(text: str) -> int:
    grid, neighbours, _, end = create_grid(text)
    starts = [key for key, value in grid.items() if value == 0]
    return dijkstra(neighbours, end, starts)


if __name__ == "__main__":
    print(part1(elevation))
    print(part2(elevation))
