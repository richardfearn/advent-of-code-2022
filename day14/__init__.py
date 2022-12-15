SOURCE_POS = (500, 0)


def part_1_answer(lines):
    rock_positions = parse(lines)

    lowest_rock_level = max(rock[1] for rock in rock_positions)

    sand_positions = set()
    sand_fell_into_void = False

    def is_blocked(pos):
        return (pos in rock_positions) or (pos in sand_positions)

    while not sand_fell_into_void:

        current_pos = SOURCE_POS
        keep_falling = True

        while keep_falling:

            next_pos = find_next_pos(current_pos, is_blocked)
            if next_pos is None:
                # has come to rest
                keep_falling = False
            else:
                current_pos = next_pos

            if current_pos[1] > lowest_rock_level:
                sand_fell_into_void = True
                keep_falling = False

        if not sand_fell_into_void:
            # has come to rest
            sand_positions.add(current_pos)

    return len(sand_positions)


def part_2_answer(lines):
    rock_positions = parse(lines)

    lowest_rock_level = max(rock[1] for rock in rock_positions)
    floor_level = lowest_rock_level + 2

    sand_positions = set()
    source_blocked = False

    def is_blocked(pos):
        return (pos in rock_positions) or (pos in sand_positions) or (pos[1] == floor_level)

    while not source_blocked:

        current_pos = SOURCE_POS
        keep_falling = True

        while keep_falling:

            next_pos = find_next_pos(current_pos, is_blocked)
            if next_pos is None:
                # has come to rest
                keep_falling = False
            else:
                current_pos = next_pos

        sand_positions.add(current_pos)

        if current_pos == SOURCE_POS:
            source_blocked = True

    return len(sand_positions)


def find_next_pos(current_pos, is_blocked):
    # try to move down
    next_pos = (current_pos[0], current_pos[1] + 1)

    if is_blocked(next_pos):
        # try to move down/left
        next_pos = (current_pos[0] - 1, current_pos[1] + 1)

    if is_blocked(next_pos):
        # try to move down/right
        next_pos = (current_pos[0] + 1, current_pos[1] + 1)

    if is_blocked(next_pos):
        # has come to rest
        next_pos = None

    return next_pos


def parse(lines):
    paths = [line.split(" -> ") for line in lines]
    paths = [[tuple(int(n) for n in point.split(",")) for point in path] for path in paths]
    return set.union(*[points_along_path(path) for path in paths])


def points_along_path(path):
    points = set()
    current_pos = path.pop(0)
    points.add(current_pos)
    while len(path) > 0:
        next_point = path.pop(0)
        dx = sign(next_point[0] - current_pos[0])
        dy = sign(next_point[1] - current_pos[1])
        while current_pos != next_point:
            current_pos = (current_pos[0] + dx, current_pos[1] + dy)
            points.add(current_pos)
    return points


def sign(x):
    return 0 if (x == 0) else (x // abs(x))
