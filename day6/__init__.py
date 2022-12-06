def part_1_answer(buffer):
    return find_marker(buffer, 4)


def part_2_answer(buffer):
    return find_marker(buffer, 14)


def find_marker(buffer, marker_length):
    for i in range(len(buffer) - marker_length - 1):
        chars = buffer[i:i + marker_length]
        if len(set(chars)) == marker_length:
            return i + marker_length
    return None
