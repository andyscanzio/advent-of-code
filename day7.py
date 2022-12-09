import os
from pprint import pprint

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

test = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

with open(os.path.join(__location__, "input.txt"), "r") as f:
    cmds = f.read().split("\n")

# cmds = test.split("\n")

stack: list[str] = []

tree: dict[str, int] = {"/": 0}

flds = {"/"}

for cmd in cmds:
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

pprint(tree)
tot_size = {fld: sum(tree[i] for i in tree.keys() if fld in i) for fld in flds}
pprint(tot_size)
print(sum(size for size in tot_size.values() if size < 100000))

free = 70000000 - tot_size["/"]
need = 30000000 - free
print(free, need)

print(min(size for size in tot_size.values() if size >= need))
