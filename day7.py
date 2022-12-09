import aoc

cmds = aoc.load_input("day7")


def get_tot_size(text: str) -> dict[str, int]:
    stack: list[str] = []

    tree: dict[str, int] = {"/": 0}

    flds = {"/"}

    for cmd in text.split("\n"):
        if "$ cd" in cmd:
            _, _, fld = cmd.split(" ")
            if fld == "/":
                stack = ["/"]
            elif fld == "..":
                stack = stack[:-1]
            else:
                stack.append(fld)
        elif cmd == "$ ls":
            continue
        elif "dir" in cmd:
            _, name = cmd.split(" ")
            path = ("/".join(stack).replace("//", "/") + f"/{name}").replace("//", "/")
            flds.add(path)
        else:
            size, _ = cmd.split(" ")
            path = "/".join(stack).replace("//", "/")
            if path not in tree:
                tree[path] = 0
            tree[path] += int(size)

    return {fld: sum(tree[i] for i in tree.keys() if fld in i) for fld in flds}


def part1(text: str) -> int:
    tot_size = get_tot_size(text)
    return sum(size for size in tot_size.values() if size < 100000)


def part2(text: str) -> int:
    tot_size = get_tot_size(text)
    free = 70000000 - tot_size["/"]
    need = 30000000 - free

    return min(size for size in tot_size.values() if size >= need)


if __name__ == "__main__":
    print(part1(cmds))
    print(part2(cmds))
