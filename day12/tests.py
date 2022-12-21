import unittest

import day12
import utils

PART_1_EXAMPLE = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(31, day12.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(425, day12.part_1_answer(utils.read_input_lines(12)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(29, day12.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(418, day12.part_2_answer(utils.read_input_lines(12)))
