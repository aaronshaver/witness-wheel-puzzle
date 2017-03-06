#!/usr/bin/python3

from puzzle import Puzzle
import unittest


class TestPuzzle(unittest.TestCase):
    def test_hello(self):
        self.assertEqual('hello', Puzzle.hello())
