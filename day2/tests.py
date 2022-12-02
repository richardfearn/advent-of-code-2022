import unittest

import day2
import utils

PART_1_EXAMPLE = """
A Y
B X
C Z
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(15, day2.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(11475, day2.part_1_answer(utils.read_input_lines(2)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(12, day2.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(16862, day2.part_2_answer(utils.read_input_lines(2)))
