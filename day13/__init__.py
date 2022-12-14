from functools import cmp_to_key
from math import prod
import utils

DIVIDER_PACKETS = """
[[2]]
[[6]]
"""


def part_1_answer(lines):
    pairs = utils.group_lines(lines)
    pairs = [[parse(packet) for packet in pair] for pair in pairs]

    return sum((i + 1) for i, pair in enumerate(pairs) if in_order(pair))


def in_order(pair):
    return compare_packets(*pair) <= 0


def compare_packets(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        return p1 - p2

    if isinstance(p1, list) and isinstance(p2, list):
        i1 = i2 = 0
        while (i1 < len(p1)) and (i2 < len(p2)):
            result = compare_packets(p1[i1], p2[i2])
            if result != 0:
                return result
            i1 += 1
            i2 += 1
        return len(p1) - len(p2)

    if isinstance(p1, int):
        p1 = [p1]
    if isinstance(p2, int):
        p2 = [p2]
    return compare_packets(p1, p2)


def part_2_answer(lines):
    packets = [parse(line) for line in lines if len(line) > 0]

    divider_packets = [parse(packet) for packet in utils.to_lines(DIVIDER_PACKETS)]
    packets.extend(divider_packets)

    packets.sort(key=cmp_to_key(compare_packets))
    return prod((packets.index(p) + 1) for p in divider_packets)


def parse(line):
    # pylint: disable=eval-used
    return eval(line)
