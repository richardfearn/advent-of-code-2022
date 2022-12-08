import unittest

import day8
import utils

PART_1_EXAMPLE = """
30373
25512
65332
33549
35390
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(21, day8.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1700, day8.part_1_answer(utils.read_input_lines(8)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(8, day8.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(470596, day8.part_2_answer(utils.read_input_lines(8)))
