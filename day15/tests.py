import unittest

import day15
import utils

PART_1_EXAMPLE = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(26, day15.part_1_answer(utils.to_lines(PART_1_EXAMPLE), 10))

    def test_with_input(self):
        self.assertEqual(5870800, day15.part_1_answer(utils.read_input_lines(15), 2000000))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(56000011, day15.part_2_answer(utils.to_lines(PART_1_EXAMPLE), 20))

    def test_with_input(self):
        self.assertEqual(10908230916597, day15.part_2_answer(utils.read_input_lines(15), 4000000))
