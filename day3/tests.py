import unittest

import day3
import utils

PART_1_EXAMPLE = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(157, day3.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(8185, day3.part_1_answer(utils.read_input_lines(3)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(70, day3.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(2817, day3.part_2_answer(utils.read_input_lines(3)))
