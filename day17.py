from functools import cache
from itertools import zip_longest

from tqdm import tqdm

import utils

jets = utils.load_input("day17")
ROCKS = [
    [0b0011110],
    [0b0001000, 0b0011100, 0b0001000],
    [0b0011100, 0b0000100, 0b0000100],  # bottom up!
    [0b0010000, 0b0010000, 0b0010000, 0b0010000],
    [0b0011000, 0b0011000],
]

TOWER_CUTOFF_LENGTH = 40

State = tuple[tuple[int, ...], int, int]


@cache
def simulate_single_step(
    tower: tuple[int, ...], piece: tuple[int, ...], command: str
) -> tuple[tuple[int, ...], bool]:
    if command == ">":
        if not any(line & 0b0000001 for line in piece) and not any(
            (pl >> 1) & tl for (pl, tl) in zip(piece, tower)
        ):
            piece = tuple((line >> 1 for line in piece))
    else:  # command == "<"
        if not any(line & 0b1000000 for line in piece) and not any(
            (pl << 1) & tl for (pl, tl) in zip(piece, tower)
        ):
            piece = tuple((line << 1 for line in piece))
    if (
        any(
            t & p for t, p in zip_longest([0b1111111] + list(tower), piece, fillvalue=0)
        )
        or piece[0]
    ):
        return (piece, True)
    else:
        return (piece[1:], False)


@cache
def simulate_piece(
    commands: str, tower: tuple[int, ...], piece_index: int, command_index: int
) -> tuple[State, int]:
    piece = tuple([0] * len(tower) + [0, 0, 0] + ROCKS[piece_index])
    terminated = False
    while not terminated:
        piece, terminated = simulate_single_step(tower, piece, commands[command_index])
        command_index = (command_index + 1) % len(commands)
    new_tower = tuple([t | p for t, p in zip_longest(tower, piece, fillvalue=0)])
    return (
        (
            new_tower[-TOWER_CUTOFF_LENGTH:],
            (piece_index + 1) % len(ROCKS),
            command_index,
        ),
        len(new_tower) - len(tower),
    )


@cache
def simulate_pieces(
    commands: str, npieces: int, state: State = ((), 0, 0)
) -> tuple[State, int]:
    height = 0
    for _ in range(npieces):
        state, delta_height = simulate_piece(commands, *state)
        height += delta_height
    return (state, height)


# Part 1
def part1(text: str, size: int) -> int:
    _, height = simulate_pieces(text, size)
    return height


# Part 2
def part2(text: str, size: int) -> int:
    stepsize = 100_000
    state = ((), 0, 0)
    height = 0
    for _ in tqdm(range(int(size / stepsize))):
        state, delta_height = simulate_pieces(text, stepsize, state)
        height += delta_height
    return height


if __name__ == "__main__":
    print(part1(jets, 2022))
    print(part2(jets, 1000000000000))
