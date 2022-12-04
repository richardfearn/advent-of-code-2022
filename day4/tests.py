import unittest

import day4
import utils

PART_1_EXAMPLE = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(2, day4.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(511, day4.part_1_answer(utils.read_input_lines(4)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(4, day4.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(821, day4.part_2_answer(utils.read_input_lines(4)))
