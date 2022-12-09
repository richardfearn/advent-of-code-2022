import unittest

import day9
import utils

PART_1_EXAMPLE = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

PART_2_EXAMPLE = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(13, day9.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(6081, day9.part_1_answer(utils.read_input_lines(9)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(36, day9.part_2_answer(utils.to_lines(PART_2_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(2487, day9.part_2_answer(utils.read_input_lines(9)))
