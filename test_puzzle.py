#!/usr/bin/python3

from puzzle import *
import unittest


class TestPuzzle(unittest.TestCase):
    def setUp(self):
        self.one_node_one_exit = {'a': ['aExit']}
        self.two_nodes_two_exits = {
            'a': ['b', 'aExit'],
            'b': ['a', 'bExit']
        }
        self.three_nodes_two_exits = {
            'a': ['b', 'c', 'aExit'],
            'b': ['a', 'c', 'bExit'],
            'c': ['a', 'b']
        }
        self.three_nodes_three_exits = {
            'a': ['b', 'c', 'aExit'],
            'b': ['a', 'c', 'bExit'],
            'c': ['a', 'b', 'cExit']
        }
        self.four_nodes_three_exits = {
            'a': ['b', 'c', 'd', 'aExit'],
            'b': ['a', 'c', 'bExit'],
            'c': ['d', 'b', 'a'],
            'd': ['a', 'c', 'dExit']
        }
        self.four_nodes_four_exits = {
            'a': ['b', 'c', 'd', 'aExit'],
            'b': ['a', 'c', 'bExit'],
            'c': ['d', 'b', 'a', 'cExit'],
            'd': ['a', 'c', 'dExit']
        }
        self.four_nodes_four_exits_max_connections = {
            'a': ['b', 'c', 'd', 'aExit'],
            'b': ['a', 'c', 'd', 'bExit'],
            'c': ['d', 'b', 'a', 'cExit'],
            'd': ['a', 'c', 'b', 'dExit']
        }
        self.five_nodes_five_exits_max_connections = {
            'a': ['b', 'c', 'd', 'e', 'aExit'],
            'b': ['a', 'c', 'd', 'e', 'bExit'],
            'c': ['d', 'b', 'a', 'e', 'cExit'],
            'd': ['a', 'c', 'b', 'e', 'dExit'],
            'e': ['a', 'c', 'b', 'd', 'eExit']
        }
        self.the_witness_seven_nodes_six_exits = {
            'a': ['b', 'f', 'g', 'aExit'],
            'b': ['a', 'c', 'g', 'bExit'],
            'c': ['b', 'd', 'g', 'cExit'],
            'd': ['c', 'e', 'g', 'dExit'],
            'e': ['d', 'f', 'g', 'eExit'],
            'f': ['e', 'a', 'g', 'fExit'],
            'g': ['a', 'b', 'c', 'd', 'e', 'f']
        }
        self.puzzle = Puzzle()

    def test_solve_single_node_single_exit(self):
        self.assertEqual(1, len(self.puzzle.solve(
            self.one_node_one_exit)))

    def test_solve_two_nodes_two_exits(self):
        self.assertEqual(4, len(self.puzzle.solve(
            self.two_nodes_two_exits)))

    def test_solve_three_nodes_two_exits(self):
        self.assertEqual(10, len(self.puzzle.solve(
            self.three_nodes_two_exits)))

    def test_solve_three_nodes_three_exits(self):
        self.assertEqual(15, len(self.puzzle.solve(
            self.three_nodes_three_exits)))

    def test_solve_four_nodes_three_exits(self):
        self.assertEqual(32, len(self.puzzle.solve(
            self.four_nodes_three_exits)))

    def test_solve_four_nodes_four_exits(self):
        self.assertEqual(42, len(self.puzzle.solve(
            self.four_nodes_four_exits)))

    def test_solve_four_nodes_four_exits_max_connections(self):
        self.assertEqual(64, len(self.puzzle.solve(
            self.four_nodes_four_exits_max_connections)))

    def test_solve_five_nodes_five_exits_max_connections(self):
        self.assertEqual(325, len(self.puzzle.solve(
            self.five_nodes_five_exits_max_connections)))

    def test_solve_the_witness_seven_nodes_six_exits(self):
        self.assertEqual(642, len(self.puzzle.solve(
            self.the_witness_seven_nodes_six_exits)))
