import unittest

import day6
import utils

PART_1_EXAMPLES = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
]

PART_2_EXAMPLES = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
]


class Part1Tests(unittest.TestCase):

    def test_examples(self):
        for buffer, start_of_packet in PART_1_EXAMPLES:
            with self.subTest(buffer=buffer, start_of_packet=start_of_packet):
                self.assertEqual(start_of_packet, day6.part_1_answer(buffer))

    def test_with_input(self):
        self.assertEqual(1356, day6.part_1_answer(utils.read_input(6)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        for buffer, start_of_message in PART_2_EXAMPLES:
            with self.subTest(buffer=buffer, start_of_message=start_of_message):
                self.assertEqual(start_of_message, day6.part_2_answer(buffer))

    def test_with_input(self):
        self.assertEqual(2564, day6.part_2_answer(utils.read_input(6)))
