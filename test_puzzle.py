#!/usr/bin/python3

from puzzle import *
import unittest


class TestPuzzle(unittest.TestCase):
    def setUp(self):
        self.a_graph = {'a': ['aExit']}
        self.ab_graph = {
            'a': ['b', 'aExit'],
            'b': ['a', 'bExit']
        }
        self.puzzle = Puzzle()

    def test_solve_single_node_single_exit(self):
        self.assertEqual('Unique paths: 1.', self.puzzle.solve(self.a_graph))

    def test_solve_two_nodes_two_exits(self):
        self.assertEqual('Unique paths: 4.', self.puzzle.solve(
            self.ab_graph))
