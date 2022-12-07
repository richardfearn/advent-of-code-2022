from collections import namedtuple

Directory = namedtuple("Directory", ["parent", "directories", "files"])

TOTAL_SPACE = 70000000
REQUIRED_UNUSED_SPACE = 30000000


def part_1_answer(lines):
    filesystem = parse(lines)

    total_sizes = []
    find_total_sizes(filesystem, [], total_sizes)

    return sum(size for size, name in total_sizes if size <= 100000)


def part_2_answer(lines):
    filesystem = parse(lines)

    total_sizes = []
    find_total_sizes(filesystem, [], total_sizes)
    total_sizes.sort()

    current_size = total_sizes[-1][0]

    for size, _ in total_sizes:
        used_after_deletion = current_size - size
        if used_after_deletion + REQUIRED_UNUSED_SPACE <= TOTAL_SPACE:
            return size

    return None


def parse(lines):
    commands = []

    for line in lines:
        if line.startswith("$"):
            command = line[2:]
            commands.append([command, []])
        else:
            commands[-1][1].append(line)

    filesystem = Directory(None, {}, {})

    current_dir = filesystem

    for command, output in commands:

        if command.startswith("cd"):
            name = command.split(" ")[1]
            if name == "/":
                current_dir = filesystem
            elif name == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.directories[name]

        elif command == "ls":
            for child in output:
                if child.startswith("dir"):
                    name = child.split(" ")[1]
                    current_dir.directories[name] = Directory(current_dir, {}, {})
                else:
                    size, name = child.split(" ")
                    current_dir.files[name] = int(size)

    return filesystem


def find_total_sizes(node, path, total_sizes):
    total_size = calc_total_size(node)
    total_sizes.append((total_size, path))

    for dir_name, dir_node in node.directories.items():
        find_total_sizes(dir_node, path + [dir_name], total_sizes)


def calc_total_size(node):
    return sum(calc_total_size(subdir) for subdir in node.directories.values()) + \
           sum(node.files.values())
