import re
from collections import namedtuple

READING_REGEX = r"Sensor at x=([-\d]+), y=([-\d]+): closest beacon is at x=([-\d]+), y=([-\d]+)"

Reading = namedtuple("Reading", ["sensor", "beacon", "distance"])

Position = namedtuple("Position", ["x", "y"])


def part_1_answer(lines, row):
    readings = parse(lines)

    ranges = row_ranges(readings, row)

    not_beacon = sum(len(r) for r in ranges)

    beacons = set(reading.beacon for reading in readings)
    for beacon in beacons:
        if (beacon.y == row) and any(beacon.x in r for r in ranges):
            not_beacon -= 1

    return not_beacon


def part_2_answer(lines, search_size):
    readings = parse(lines)

    distress_beacon_pos = None

    for y in range(search_size):

        ranges = row_ranges(readings, y)

        if len(ranges) == 1:
            for x in (0, search_size - 1):
                if x not in ranges[0]:
                    distress_beacon_pos = Position(x, y)

        if len(ranges) == 2:
            distress_beacon_pos = Position(ranges[0].stop, y)

        if distress_beacon_pos is not None:
            break

    return distress_beacon_pos.x * 4000000 + distress_beacon_pos.y


def row_ranges(readings, y):
    ranges = [row_range(reading, y) for reading in readings]
    ranges = [r for r in ranges if r is not None]
    return merge_ranges(ranges)


def row_range(reading, y):
    sensor, _, distance = reading

    if (sensor.y - distance) <= y <= (sensor.y + distance):
        row_size = distance - abs(y - sensor.y)
        start = sensor.x - row_size
        end = sensor.x + row_size
        return range(start, end + 1)

    return None


def merge_ranges(ranges):
    # https://www.geeksforgeeks.org/merging-intervals/

    ranges.sort(key=lambda x: x.start)

    merged = [ranges[0]]
    for r in ranges[1:]:
        if merged[-1].start <= r.start <= merged[-1].stop:
            merged[-1] = range(merged[-1].start, max(merged[-1].stop, r.stop))
        else:
            merged.append(r)

    return merged


def parse(lines):
    return [parse_line(line) for line in lines]


def parse_line(line):
    m = re.match(READING_REGEX, line)
    sensor_pos = Position(int(m.group(1)), int(m.group(2)))
    beacon_pos = Position(int(m.group(3)), int(m.group(4)))
    distance = abs(beacon_pos.x - sensor_pos.x) + abs(beacon_pos.y - sensor_pos.y)
    return Reading(sensor_pos, beacon_pos, distance)
