def part_1_answer(lines):
    def one_contains_the_other(ranges):
        a, b = ranges
        return (a[0] <= b[0] and b[1] <= a[1]) or (b[0] <= a[0] and a[1] <= b[1])

    return sum(one_contains_the_other(pair) for pair in parse(lines))


def part_2_answer(lines):
    def ranges_overlap(ranges):
        a, b = ranges
        return (a[0] <= b[0] <= a[1]) or (b[0] <= a[0] <= b[1])

    return sum(ranges_overlap(pair) for pair in parse(lines))


def parse(lines):
    pairs = [line.split(",") for line in lines]
    pairs = [[assignment.split("-") for assignment in pair] for pair in pairs]
    pairs = [[[int(section) for section in assignment] for assignment in pair] for pair in pairs]
    return pairs
