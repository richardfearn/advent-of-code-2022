import unittest

import day13
import utils

PART_1_EXAMPLE = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(13, day13.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(6076, day13.part_1_answer(utils.read_input_lines(13)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(140, day13.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(24805, day13.part_2_answer(utils.read_input_lines(13)))
