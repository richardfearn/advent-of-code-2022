import unittest

import day7
import utils

PART_1_EXAMPLE = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(95437, day7.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1297159, day7.part_1_answer(utils.read_input_lines(7)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(24933642, day7.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(3866390, day7.part_2_answer(utils.read_input_lines(7)))
