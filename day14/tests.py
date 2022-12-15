import unittest

import day14
import utils

PART_1_EXAMPLE = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(24, day14.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(592, day14.part_1_answer(utils.read_input_lines(14)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(93, day14.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(30367, day14.part_2_answer(utils.read_input_lines(14)))
