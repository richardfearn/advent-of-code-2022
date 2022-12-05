import unittest

import day5
import utils

PART_1_EXAMPLE = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual("CMZ", day5.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual("JDTMRWCQJ", day5.part_1_answer(utils.read_input_lines(5)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual("MCD", day5.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual("VHJDDCWRD", day5.part_2_answer(utils.read_input_lines(5)))
