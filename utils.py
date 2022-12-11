from pathlib import Path


def load_input(day: str) -> str:
    path = Path.cwd() / Path(f"inputs/input_{day}.txt")
    with open(path, "r") as f:
        return f.read()
