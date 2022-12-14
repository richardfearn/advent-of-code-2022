import math
import operator
from collections import deque, namedtuple
import utils

Monkey = namedtuple("Monkey", ["items", "operation", "test", "if_true", "if_false"])

OPERATORS = {
    "*": operator.mul,
    "+": operator.add,
}


def part_1_answer(lines):
    return run(lines, 1, 20)


def part_2_answer(lines):
    return run(lines, 2, 10000)


def run(lines, part, rounds):
    monkeys = parse(lines)

    test_numbers = list(monkey.test for monkey in monkeys)
    test_num_product = math.prod(test_numbers)

    inspections = [0] * len(monkeys)

    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            inspections[i] += len(monkey.items)

            while len(monkey.items) > 0:
                worry_level = monkey.items.popleft()

                worry_level = monkey.operation(worry_level)

                if part == 1:
                    worry_level //= 3
                elif part == 2:
                    worry_level %= test_num_product

                if (worry_level % monkey.test) == 0:
                    throw_to = monkey.if_true
                else:
                    throw_to = monkey.if_false

                monkeys[throw_to].items.append(worry_level)

    return math.prod(sorted(inspections, reverse=True)[:2])


def parse(lines):
    groups = utils.group_lines(lines)
    return [parse_group(group) for group in groups]


def parse_group(group):
    starting_items = [int(n) for n in group[1].split(": ")[1].split(", ")]
    operation = group[2].lstrip().split(" ")[-3:]
    test = int(group[3].lstrip().split(" ")[-1])
    if_true = int(group[4].lstrip().split(" ")[-1])
    if_false = int(group[5].lstrip().split(" ")[-1])

    def operation_function(worry_level):
        arg1 = worry_level if (operation[0] == "old") else int(operation[0])
        arg2 = worry_level if (operation[2] == "old") else int(operation[2])
        return OPERATORS[operation[1]](arg1, arg2)

    return Monkey(deque(starting_items), operation_function, test, if_true, if_false)
