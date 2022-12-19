from typing import Any

import mip as mip  # type: ignore
from parse import parse  # type: ignore

import utils

bprints = utils.load_input("day19")


def check_blueprint(mins: int, blueprint: dict[str, int]) -> int:
    model = mip.Model(sense=mip.MAXIMIZE)
    obj = mip.LinExpr(0)  # type: ignore
    vars_all: list[dict[str, Any]] = []
    for m in range(mins):
        vars: dict[str, Any] = {}
        vars.update({"ore": model.add_var(f"ore_{m}", var_type=mip.BINARY)})
        vars.update({"clay": model.add_var(f"clay_{m}", var_type=mip.BINARY)})
        vars.update({"obs": model.add_var(f"obs_{m}", var_type=mip.BINARY)})
        vars.update({"geo": model.add_var(f"geo_{m}", var_type=mip.BINARY)})
        vars_all.append(vars)

        model.add_constr(vars["ore"] + vars["clay"] + vars["obs"] + vars["geo"] <= 1)  # type: ignore

        ore = mip.LinExpr(const=m)  # type: ignore
        clay = mip.LinExpr(const=0)  # type: ignore
        obs = mip.LinExpr(const=0)  # type: ignore
        for m_ in range(m):
            ore.add_var(vars_all[m_]["ore"], m - m_ - 1)  # type: ignore
            ore.add_var(vars_all[m_]["ore"], -blueprint["oror"])  # type: ignore
            ore.add_var(vars_all[m_]["clay"], -blueprint["clor"])  # type: ignore
            ore.add_var(vars_all[m_]["obs"], -blueprint["obor"])  # type: ignore
            ore.add_var(vars_all[m_]["geo"], -blueprint["geor"])  # type: ignore

            clay.add_var(vars_all[m_]["clay"], m - m_ - 1)  # type: ignore
            clay.add_var(vars_all[m_]["obs"], -blueprint["obcl"])  # type: ignore

            obs.add_var(vars_all[m_]["obs"], m - m_ - 1)  # type: ignore
            obs.add_var(vars_all[m_]["geo"], -blueprint["geob"])  # type: ignore

        model.add_constr(  # type: ignore
            ore
            >= vars["ore"] * blueprint["oror"]
            + vars["clay"] * blueprint["clor"]
            + vars["obs"] * blueprint["obor"]
            + vars["geo"] * blueprint["geor"]
        )
        model.add_constr(clay >= vars["obs"] * blueprint["obcl"])  # type: ignore
        model.add_constr(obs >= vars["geo"] * blueprint["geob"])  # type: ignore

        obj.add_var(vars["geo"], mins - m - 1)  # type: ignore

    model.objective = obj
    model.verbose = 0
    model.optimize()

    return int(model.objective_value)  # type: ignore


def part1(text: str) -> int:
    mins = 24
    blueprints: list[dict[str, int]] = []
    score: list[int] = []

    for l in text.splitlines():
        vars = parse(
            "Blueprint {i}: Each ore robot costs {oror} ore. Each clay robot costs {clor} ore. Each obsidian robot costs {obor} ore and {obcl} clay. Each geode robot costs {geor} ore and {geob} obsidian.",
            l.strip(),
        )
        if vars is not None:
            blueprints.append({k: int(v) for k, v in vars.named.items()})  # type: ignore

    for blueprint in blueprints:
        val = check_blueprint(mins, blueprint)
        score.append(val * blueprint["i"])
    return sum(score)


def part2(text: str) -> int:
    mins = 32
    blueprints: list[dict[str, int]] = []
    score: list[int] = []

    for l in text.splitlines():
        vars = parse(
            "Blueprint {i}: Each ore robot costs {oror} ore. Each clay robot costs {clor} ore. Each obsidian robot costs {obor} ore and {obcl} clay. Each geode robot costs {geor} ore and {geob} obsidian.",
            l.strip(),
        )
        if vars is not None:
            blueprints.append({k: int(v) for k, v in vars.named.items()})  # type: ignore

    for blueprint in blueprints[:3]:
        val = check_blueprint(mins, blueprint)
        score.append(val)
    return score[0] * score[1] * score[2]


if __name__ == "__main__":
    print(part1(bprints))
    print(part2(bprints))
