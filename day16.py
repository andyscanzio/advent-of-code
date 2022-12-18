import re

import utils

scan = utils.load_input("day16")


class Valve:
    def __init__(self, name: str, flow_rate: int, connections: set[str]):
        self.name = name
        self.flow_rate = flow_rate
        self.connections = connections

    def __repr__(self) -> str:
        return f"Valve('{self.name}', {self.flow_rate}, {self.connections})"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, type(self)):
            return (
                self.name == __o.name
                and self.flow_rate == __o.flow_rate
                and self.connections == __o.connections
            )
        return NotImplemented


def parse(puzzle_input: str) -> tuple[dict[str, Valve], dict[str, dict[str, int]]]:
    """Parse input."""
    store_dict: dict[str, Valve] = {}
    # valves = []
    prog = re.compile(
        r"Valve ([A-Z]{2}) has flow rate=(\d+); "
        r"tunnels? leads? to valves? ((([A-Z]{2}), )*([A-Z]{2}))"
    )
    for line in puzzle_input.splitlines():
        match = prog.match(line)
        if match is not None:
            name = match.group(1)
            flow_rate = int(match.group(2))
            connections = set(match.group(3).split(", "))
            valve = Valve(name, flow_rate, connections)
            # valves.append(valve)
            store_dict[name] = valve
    steps = {
        x: {
            y: 1 if y in store_dict[x].connections else 1_000_000_000
            for y in store_dict
        }
        for x in store_dict
    }
    # Floyd-Warshall Algorithm for steps between nodes (valves)
    for k in steps:
        for i in steps:
            for j in steps:
                steps[i][j] = min(steps[i][j], steps[i][k] + steps[k][j])

    # logging.debug(valves)
    return store_dict, steps  # , valves


def traveling_elf(
    valves: dict[str, Valve],
    steps: dict[str, dict[str, int]],
    last_valve: str,
    time_remaining: int,
    state_machine: dict[str, int],
    state: int,
    flow: int,
    answer: dict[int, int],
) -> dict[int, int]:
    # if opened_valves is None:
    #     opened_valves = set()
    answer[state] = max(answer.get(state, 0), flow)
    for valve in valves:
        minutes = time_remaining - steps[last_valve][valve] - 1
        # Bitmasking for state. Each bit represents valve
        if (state_machine[valve] & state) or (minutes <= 0):
            continue
        # recursion - add this valve to the state. Add this valve to the flow
        traveling_elf(
            valves,
            steps,
            valve,
            minutes,
            state_machine,
            state | state_machine[valve],
            flow + (minutes * valves[valve].flow_rate),
            answer,
        )
    return answer


def part1(text: str) -> int:
    parsed_data = parse(text)
    valve_dict, steps = parsed_data
    minutes = 30
    valves = {
        name: valve for (name, valve) in valve_dict.items() if valve.flow_rate > 0
    }
    state_machine = {v: 1 << i for i, v in enumerate(valves)}
    last_valve = "AA"
    starting_state = 0
    starting_flow = 0
    total_flow = max(
        traveling_elf(
            valves,
            steps,
            last_valve,
            minutes,
            state_machine,
            starting_state,
            starting_flow,
            {},
        ).values()
    )
    return total_flow


def part2(text: str) -> int:
    parsed_data = parse(text)
    valve_dict, steps = parsed_data
    minutes = 26
    valves = {
        name: valve for (name, valve) in valve_dict.items() if valve.flow_rate > 0
    }
    state_machine = {v: 1 << i for i, v in enumerate(valves)}
    last_valve = "AA"
    starting_state = 0
    starting_flow = 0
    paths = traveling_elf(
        valves,
        steps,
        last_valve,
        minutes,
        state_machine,
        starting_state,
        starting_flow,
        {},
    )
    total_flow = max(
        my_val + el_val
        for k1, my_val in paths.items()
        for k2, el_val in paths.items()
        if not k1 & k2
    )
    return total_flow


if __name__ == "__main__":
    print(part1(scan))
    print(part2(scan))
