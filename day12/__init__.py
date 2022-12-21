from collections import defaultdict
from heapq import heappop, heappush


def part_1_answer(lines):
    grid, start_pos, end_pos = parse(lines)
    graph = make_graph(grid)
    return shortest_path(graph, start_pos, end_pos)


def part_2_answer(lines):
    grid, _, end_pos = parse(lines)
    graph = make_graph(grid)

    start_positions = set()
    for y, row in enumerate(grid):
        for x, elevation in enumerate(row):
            if elevation == 0:
                start_positions.add((x, y))

    dists = [shortest_path(graph, start, end_pos) for start in start_positions]
    return min(d for d in dists if d)


def parse(lines):
    start_pos = end_pos = None

    for y, line in enumerate(lines):
        if "S" in line:
            x = line.index("S")
            start_pos = (x, y)
            lines[y] = line = line.replace("S", "a")
        if "E" in line:
            x = line.index("E")
            end_pos = (x, y)
            lines[y] = line = line.replace("E", "z")

    grid = [[(ord(c) - 97) for c in line] for line in lines]

    return grid, start_pos, end_pos


def make_graph(grid):
    width, height = len(grid[0]), len(grid)

    graph = defaultdict(set)

    for x in range(width):
        for y in range(height):
            elevation = grid[y][x]
            for offset in (0, -1), (0, 1), (-1, 0), (1, 0):
                nx, ny = (x + offset[0]), (y + offset[1])
                if (0 <= nx < width) and (0 <= ny < height):
                    neighbour_elevation = grid[ny][nx]
                    if (neighbour_elevation - elevation) <= 1:
                        graph[(x, y)].add((nx, ny))

    return graph


def shortest_path(graph, start_pos, end_pos):
    dist = {start_pos: 0}
    q = [(0, start_pos)]

    while len(q) > 0:
        u = heappop(q)[1]
        for v in graph[u]:
            alt = dist[u] + 1
            if (v not in dist) or (alt < dist[v]):
                dist[v] = alt
                heappush(q, (alt, v))

    return dist.get(end_pos)
