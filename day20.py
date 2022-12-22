import utils

sequences = utils.load_input("day20")


def index_of_zero(number_list: list[tuple[int, int]]) -> int:
    for i in range(len(number_list)):
        if number_list[i][1] == 0:
            return i
    return 0


def part1(text: str) -> int:
    number_list: list[tuple[int, int]] = list(enumerate(map(int, text.splitlines())))
    list_size = len(number_list)
    for i in range(list_size):
        for j in range(list_size):
            if number_list[j][0] == i:
                num = number_list[j]
                number_list.pop(j)
                if num[1] == -j:
                    number_list.append(num)
                else:
                    number_list.insert((j + num[1]) % (list_size - 1), num)
                break
    zi = index_of_zero(number_list)
    return sum(
        number_list[(zi + i) % len(number_list)][1] for i in range(1000, 4000, 1000)
    )


def part2(text: str) -> int:
    number_list: list[tuple[int, int]] = list(enumerate(map(int, text.splitlines())))
    number_list = [(a, b * 811589153) for a, b in number_list]
    list_size = len(number_list)
    for _ in range(10):
        for i in range(list_size):
            for j in range(list_size):
                if number_list[j][0] == i:
                    num = number_list[j]
                    number_list.pop(j)
                    if num[1] == -j:
                        number_list.append(num)
                    else:
                        number_list.insert((j + num[1]) % (list_size - 1), num)
                    break
    zi = index_of_zero(number_list)
    return sum(
        number_list[(zi + i) % len(number_list)][1] for i in range(1000, 4000, 1000)
    )


if __name__ == "__main__":
    print(part1(sequences))
    print(part2(sequences))
