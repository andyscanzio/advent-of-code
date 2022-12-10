import os


def load_input(day: str) -> str:
    __location__ = os.path.realpath(os.path.join(os.getcwd()))
    path = os.path.join(os.getcwd(), f"inputs/input_{day}.txt")
    with open(path, "r") as f:
        return f.read()
