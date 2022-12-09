from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

OFFSETS = {
    "L": Point(-1, 0),
    "R": Point(1, 0),
    "U": Point(0, 1),
    "D": Point(0, -1),
}


def part_1_answer(lines):
    motions = parse(lines)

    head = tail = Point(0, 0)
    visited = {tail}

    for direction, amount in motions:
        offset = OFFSETS[direction]

        for _ in range(amount):
            head = Point(head.x + offset.x, head.y + offset.y)
            tail = update_tail(tail, head)
            visited.add(tail)

    return len(visited)


def part_2_answer(lines):
    motions = parse(lines)

    knots = [Point(0, 0)] * 10
    visited = {knots[-1]}

    for direction, amount in motions:
        offset = OFFSETS[direction]

        for _ in range(amount):
            knots[0] = Point(knots[0].x + offset.x, knots[0].y + offset.y)
            for i in range(1, 10):
                knots[i] = update_tail(knots[i], knots[i - 1])
            visited.add(knots[-1])

    return len(visited)


def update_tail(tail, head):
    dx = dy = 0

    if (head.x == tail.x) and (abs(tail.y - head.y) == 2):
        # head directly 2 steps up/down from tail
        dx = 0
        dy = 1 if (tail.y < head.y) else -1

    elif (abs(tail.x - head.x) == 2) and (head.y == tail.y):
        # head directly 2 steps left/right from tail
        dx = 1 if (tail.x < head.x) else -1
        dy = 0

    elif (abs(tail.x - head.x) == 2) or (abs(tail.y - head.y) == 2):
        # not touching; not in same row/column; move diagonally
        dx = 1 if (tail.x < head.x) else -1
        dy = 1 if (tail.y < head.y) else -1

    return Point(tail.x + dx, tail.y + dy)


def parse(lines):
    motions = [line.split(" ") for line in lines]
    motions = [(line[0], int(line[1])) for line in motions]
    return motions
