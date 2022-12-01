import unittest

import day1
import utils

PART_1_EXAMPLE = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(24000, day1.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(69289, day1.part_1_answer(utils.read_input_lines(1)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(45000, day1.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(205615, day1.part_2_answer(utils.read_input_lines(1)))
