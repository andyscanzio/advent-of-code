import utils

instructions = utils.load_input("day10")


def part1(text: str) -> int:
    stack: list[str] = text.split("\n")[::-1]
    signal: list[int] = []
    x = 1
    cycle = 1
    working = False
    reg = 0
    cmd = ""
    while stack:
        cycle += 1
        if not working:
            cmd = stack.pop()
            if "addx" in cmd:
                reg = int(cmd.split(" ")[1])
                working = True
        else:
            x += reg
            reg = 0
            working = False
        if (cycle - 20) % 40 == 0:
            signal.append(cycle * x)
    return sum(signal)


def draw_pixel(cycle: int, x: int, crt: str) -> str:
    pixel = (cycle - 1) % 40
    if x - 1 <= pixel <= x + 1:
        crt += "#"
    else:
        crt += "."
    if (cycle) % 40 == 0:
        crt += "\n"
    return crt


def part2(text: str) -> str:
    stack: list[str] = text.split("\n")[::-1]
    x = 1
    cycle = 1
    reg = 0
    cmd = ""
    crt = ""
    while stack:
        cmd = stack.pop()
        if "noop" in cmd:
            crt = draw_pixel(cycle, x, crt)
        elif "addx" in cmd:
            reg = int(cmd.split(" ")[1])
            crt = draw_pixel(cycle, x, crt)
            cycle += 1
            crt = draw_pixel(cycle, x, crt)
            x += reg
        cycle += 1
    return crt.rstrip("\n")


if __name__ == "__main__":
    print(part1(instructions))
    print(part2(instructions))
