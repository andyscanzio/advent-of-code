from fractions import Fraction
from operator import add, floordiv, mul, sub

import utils

monkeys = utils.load_input("day21")


def part1(text: str) -> int:
    monkeys: dict[str, tuple[str] | tuple[str, str, str] | int] = {}
    for line in text.splitlines():
        split = line.split(": ")
        monkeys[split[0]] = tuple(split[1].split(" "))
    while True:
        root = monkeys["root"]
        if isinstance(root, int):
            return root
        for key in monkeys.keys():
            temp = monkeys[key]
            if isinstance(temp, tuple):
                if len(temp) == 1:
                    monkeys[key] = int(temp[0])
                else:
                    left, op, right = temp
                    if not isinstance(monkeys[left], int):
                        continue
                    elif not isinstance(monkeys[right], int):
                        continue
                    else:
                        if op == "+":
                            f = add
                        elif op == "-":
                            f = sub
                        elif op == "*":
                            f = mul
                        else:
                            f = floordiv
                        monkeys[key] = f(monkeys[left], monkeys[right])


def part2(text: str) -> int:
    definitions: dict[str, int | tuple[str, str, str]] = {}
    for line in text.splitlines():
        name, definition = line.split(": ", maxsplit=1)
        try:
            definitions[name] = int(definition)
        except ValueError:
            definitions[name] = tuple(definition.rstrip().split(maxsplit=2))

    def evaluate(name: str) -> tuple[Fraction, Fraction] | None:
        if name == "humn":
            return Fraction(1), Fraction(0)
        match definitions[name]:
            case value if isinstance(value, int):
                return Fraction(0), Fraction(value)
            case (lhs, "+", rhs):
                l, r = evaluate(lhs), evaluate(rhs)
                if l is not None:
                    slope1, intercept1 = l
                else:
                    slope1, intercept1 = Fraction(1), Fraction(0)
                if r is not None:
                    slope2, intercept2 = r
                else:
                    slope2, intercept2 = Fraction(1), Fraction(0)
                return slope1 + slope2, intercept1 + intercept2
            case (lhs, "-", rhs):
                l, r = evaluate(lhs), evaluate(rhs)
                if l is not None:
                    slope1, intercept1 = l
                else:
                    slope1, intercept1 = Fraction(1), Fraction(0)
                if r is not None:
                    slope2, intercept2 = r
                else:
                    slope2, intercept2 = Fraction(1), Fraction(0)
                return slope1 - slope2, intercept1 - intercept2
            case (lhs, "*", rhs):
                l, r = evaluate(lhs), evaluate(rhs)
                if l is not None:
                    slope1, intercept1 = l
                else:
                    slope1, intercept1 = Fraction(1), Fraction(0)
                if r is not None:
                    slope2, intercept2 = r
                else:
                    slope2, intercept2 = Fraction(1), Fraction(0)
                if not slope1:
                    return intercept1 * slope2, intercept1 * intercept2
                if not slope2:
                    return slope1 * intercept2, intercept1 * intercept2
            case (lhs, "/", rhs):
                l, r = evaluate(lhs), evaluate(rhs)
                if l is not None:
                    slope1, intercept1 = l
                else:
                    slope1, intercept1 = Fraction(1), Fraction(1)
                if r is not None:
                    slope2, intercept2 = r
                else:
                    slope2, intercept2 = Fraction(1), Fraction(1)
                if not slope2:
                    return slope1 / intercept2, intercept1 / intercept2
            case _:
                pass

    root = definitions["root"]
    if isinstance(root, tuple):
        lhs, _, rhs = root
        l, r = evaluate(lhs), evaluate(rhs)
        if l is not None:
            slope1, intercept1 = l
        else:
            slope1, intercept1 = Fraction(1), Fraction(0)
        if r is not None:
            slope2, intercept2 = r
        else:
            slope2, intercept2 = Fraction(1), Fraction(0)
        x = (intercept2 - intercept1) / (slope1 - slope2)
        assert x.denominator == 1
        return int(x)
    return 0


if __name__ == "__main__":
    print(part1(monkeys))
    print(part2(monkeys))
