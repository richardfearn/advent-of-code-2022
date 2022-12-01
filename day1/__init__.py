import utils


def part_1_answer(lines):
    return max(totals(lines))


def part_2_answer(lines):
    return sum(sorted(totals(lines), reverse=True)[:3])


def totals(lines):
    groups = utils.group_lines(lines)
    groups = [[int(n) for n in group] for group in groups]
    return [sum(group) for group in groups]
