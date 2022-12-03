from functools import reduce


def part_1_answer(lines):
    def common_item(rucksack):
        mid = len(rucksack) // 2
        first, second = set(rucksack[:mid]), set(rucksack[mid:])
        return next(iter(first.intersection(second)))

    return sum(priority(common_item(rucksack)) for rucksack in lines)


def part_2_answer(lines):
    def common_item(rucksacks):
        rucksacks = [set(r) for r in rucksacks]
        common_items = reduce(set.intersection, rucksacks)
        return next(iter(common_items))

    return sum(priority(common_item(lines[i:i + 3])) for i in range(0, len(lines), 3))


def priority(c):
    return (ord(c) - 96) if ("a" <= c <= "z") else (ord(c) - 64 + 26)
