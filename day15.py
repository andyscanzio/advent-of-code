import utils

sensors = utils.load_input("day15")


def mdist(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part1(text: str, row: int) -> int:
    sensors: list[tuple[int, int, int, int]] = []
    for line in text.splitlines():
        match line.replace(":", "").replace(",", "").split(" "):
            case "Sensor", "at", _xs, _ys, "closest", "beacon", "is", "at", _xb, _yb:
                xs = int(_xs.split("=")[1])
                ys = int(_ys.split("=")[1])
                xb = int(_xb.split("=")[1])
                yb = int(_yb.split("=")[1])
                sensors.append((xs, ys, xb, yb))
            case _:
                pass
    intervals: list[tuple[int, int]] = []
    for sx, sy, bx, by in sensors:
        dx = abs(sx - bx) + abs(sy - by) - abs(sy - row)
        if dx >= 0:
            intervals.append((sx - dx, sx + dx))
    l, r = zip(*intervals)
    beacons = len(set(bx for _, _, bx, by in sensors if by == row))
    return max(r) + 1 - min(l) - beacons


def part2(text: str, size: int) -> int:
    def border(x: int, y: int, radius: int):
        for dx in range(radius + 2):
            dy = radius + 1 - dx
            yield x + dx, y + dy
            yield x + dx, y - dy
            yield x - dx, y + dy
            yield x - dx, y - dy

    sensors: list[tuple[int, int, int, int]] = []
    for line in text.splitlines():
        match line.replace(":", "").replace(",", "").split(" "):
            case "Sensor", "at", _xs, _ys, "closest", "beacon", "is", "at", _xb, _yb:
                xs = int(_xs.split("=")[1])
                ys = int(_ys.split("=")[1])
                xb = int(_xb.split("=")[1])
                yb = int(_yb.split("=")[1])
                sensors.append((xs, ys, xb, yb))
            case _:
                pass
    rad = [(sx, sy, abs(sx - bx) + abs(sy - by)) for sx, sy, bx, by in sensors]
    for sensor in rad:
        for x, y in border(*sensor):
            if (
                0 <= x <= size
                and 0 <= y <= size
                and all(abs(x - sx) + abs(y - sy) > r for sx, sy, r in rad)
            ):
                return x * 4000000 + y
    return 0


if __name__ == "__main__":
    print(part1(sensors, 2000000))
    print(part2(sensors, 4000000))
