import math

UP, DOWN, LEFT, RIGHT = range(4)

OFFSETS = {
    UP: (0, -1),
    DOWN: (0, 1),
    LEFT: (-1, 0),
    RIGHT: (1, 0),
}


def part_1_answer(lines):
    grid, grid_size = parse(lines)
    width, height = grid_size

    visible = set()

    for y in range(height):
        visible.update(visible_across_grid(grid, grid_size, (-1, y), RIGHT))
        visible.update(visible_across_grid(grid, grid_size, (width, y), LEFT))

    for x in range(width):
        visible.update(visible_across_grid(grid, grid_size, (x, -1), DOWN))
        visible.update(visible_across_grid(grid, grid_size, (x, height), UP))

    return len(visible)


def visible_across_grid(grid, grid_size, start_pos, direction):
    w, h = grid_size
    x, y = start_pos
    dx, dy = OFFSETS[direction]

    visible = set()
    max_height = -1

    x += dx
    y += dy
    while (0 <= x < w) and (0 <= y < h):
        this_height = grid[y][x]
        if this_height > max_height:
            visible.add((x, y))
            max_height = this_height
        x += dx
        y += dy

    return visible


def part_2_answer(lines):
    grid, grid_size = parse(lines)
    width, height = grid_size

    scores = set()

    for x in range(width):
        for y in range(height):
            scores.add(scenic_score(grid, grid_size, (x, y)))

    return max(scores)


def scenic_score(grid, grid_size, pos):
    return math.prod(
        visible_from_tree(grid, grid_size, pos, direction)
        for direction in (UP, DOWN, LEFT, RIGHT))


def visible_from_tree(grid, grid_size, tree_pos, direction):
    w, h = grid_size
    x, y = tree_pos
    dx, dy = OFFSETS[direction]

    visible = 0
    start_height = grid[y][x]

    x += dx
    y += dy
    while (0 <= x < w) and (0 <= y < h):
        this_height = grid[y][x]
        visible += 1
        if this_height >= start_height:
            # view now blocked
            break
        x += dx
        y += dy

    return visible


def parse(lines):
    grid = [[int(n) for n in row] for row in lines]
    width, height = len(grid[0]), len(grid)
    return grid, (width, height)
