def part_1_answer(lines):
    return CPU(lines).run().sum_of_strengths


def part_2_answer(lines):
    return CPU(lines).run().screen


class CPU:

    def __init__(self, lines):
        self.instructions = self.parse(lines)
        self.sum_of_strengths = None
        self.screen = None

    @staticmethod
    def parse(lines):
        return [instruction.split(" ") for instruction in lines]

    def run(self):
        sum_of_strengths = 0
        screen = [["."] * 40 for _ in range(6)]

        x = 1
        cycle = 0

        for instruction in self.instructions:
            op = instruction[0]
            cycles_for_instruction = 2 if (op == "addx") else 1

            for _ in range(cycles_for_instruction):
                cycle += 1

                # Part 1
                if cycle in {20, 60, 100, 140, 180, 220}:
                    signal_strength = cycle * x
                    sum_of_strengths += signal_strength

                # Part 2
                px = (cycle - 1) % 40
                py = (cycle - 1) // 40
                if (x - 1) <= px <= (x + 1):
                    screen[py][px] = "#"

            if op == "addx":
                v = int(instruction[1])
                x += v

        self.sum_of_strengths = sum_of_strengths
        self.screen = "\n".join("".join(row) for row in screen)

        return self
