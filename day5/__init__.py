import utils


def part_1_answer(lines):
    stacks, steps = parse(lines)

    for quantity, from_stack, to_stack in steps:
        crates = stacks[from_stack][-quantity:]
        stacks[from_stack] = stacks[from_stack][:-quantity]
        stacks[to_stack] = stacks[to_stack] + crates[::-1]

    return "".join(stack[-1] for stack in stacks)


def part_2_answer(lines):
    stacks, steps = parse(lines)

    for quantity, from_stack, to_stack in steps:
        crates = stacks[from_stack][-quantity:]
        stacks[from_stack] = stacks[from_stack][:-quantity]
        stacks[to_stack] = stacks[to_stack] + crates

    return "".join(stack[-1] for stack in stacks)


def parse(lines):
    groups = utils.group_lines(lines)
    stacks, steps = groups[0], groups[1]

    num_stacks = max(int(n) for n in stacks[-1].split(" ") if n)
    stacks = stacks[:-1]
    stacks = [line.ljust(num_stacks * 4 - 1) for line in stacks]
    stacks.reverse()
    stacks = [[line[i * 4 + 1] for i in range(num_stacks)] for line in stacks]
    stacks = [[stacks[y][x] for y in range(len(stacks))] for x in range(num_stacks)]
    stacks = ["".join(stack).rstrip() for stack in stacks]

    for i, step in enumerate(steps):
        step = step.split(" ")
        quantity, from_stack, to_stack = int(step[1]), int(step[3]), int(step[5])
        steps[i] = quantity, from_stack - 1, to_stack - 1

    return stacks, steps
