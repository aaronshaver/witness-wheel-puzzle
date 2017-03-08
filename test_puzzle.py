#!/usr/bin/python3

import json
from puzzle import *
import unittest


class TestPuzzle(unittest.TestCase):
    def setUp(self):
        self.one_start_one_end = {
            'a': ['aExit']
        }
        self.two_starts_two_ends = {
            'a': ['b', 'aExit'],
            'b': ['a', 'bExit']
        }
        self.three_starts_two_ends = {
            'a': ['b', 'c', 'aExit'],
            'b': ['a', 'c', 'bExit'],
            'c': ['a', 'b']
        }
        self.three_starts_three_ends = {
            'a': ['b', 'c', 'aExit'],
            'b': ['a', 'c', 'bExit'],
            'c': ['a', 'b', 'cExit']
        }
        self.four_starts_three_ends = {
            'a': ['b', 'c', 'd', 'aExit'],
            'b': ['a', 'c', 'bExit'],
            'c': ['d', 'b', 'a'],
            'd': ['a', 'c', 'dExit']
        }
        self.four_starts_four_ends = {
            'a': ['b', 'c', 'd', 'aExit'],
            'b': ['a', 'c', 'bExit'],
            'c': ['d', 'b', 'a', 'cExit'],
            'd': ['a', 'c', 'dExit']
        }
        self.four_starts_four_ends_max_connections = {
            'a': ['b', 'c', 'd', 'aExit'],
            'b': ['a', 'c', 'd', 'bExit'],
            'c': ['d', 'b', 'a', 'cExit'],
            'd': ['a', 'c', 'b', 'dExit']
        }
        self.five_starts_five_ends_max_connections = {
            'a': ['b', 'c', 'd', 'e', 'aExit'],
            'b': ['a', 'c', 'd', 'e', 'bExit'],
            'c': ['d', 'b', 'a', 'e', 'cExit'],
            'd': ['a', 'c', 'b', 'e', 'dExit'],
            'e': ['a', 'c', 'b', 'd', 'eExit']
        }
        self.the_witness_seven_starts_six_ends = {
            'a': ['b', 'f', 'g', 'aExit'],
            'b': ['a', 'c', 'g', 'bExit'],
            'c': ['b', 'd', 'g', 'cExit'],
            'd': ['c', 'e', 'g', 'dExit'],
            'e': ['d', 'f', 'g', 'eExit'],
            'f': ['e', 'a', 'g', 'fExit'],
            'g': ['a', 'b' 'c', 'd', 'e', 'f']
        }
        self.puzzle = Puzzle()

    def test_solve_one_start_one_end(self):
        self.assertEqual(1, len(self.puzzle.solve(
            self.one_start_one_end)))

    def test_solve_two_starts_two_ends(self):
        self.assertEqual(4, len(self.puzzle.solve(
            self.two_starts_two_ends)))

    def test_solve_three_starts_two_ends(self):
        self.assertEqual(10, len(self.puzzle.solve(
            self.three_starts_two_ends)))

    def test_solve_three_starts_three_ends(self):
        self.assertEqual(15, len(self.puzzle.solve(
            self.three_starts_three_ends)))

    def test_solve_four_starts_three_ends(self):
        self.assertEqual(32, len(self.puzzle.solve(
            self.four_starts_three_ends)))

    def test_solve_four_starts_four_ends(self):
        self.assertEqual(42, len(self.puzzle.solve(
            self.four_starts_four_ends)))

    def test_solve_four_starts_four_ends_max_connections(self):
        self.assertEqual(64, len(self.puzzle.solve(
            self.four_starts_four_ends_max_connections)))

    def test_solve_five_starts_five_ends_max_connections(self):
        self.assertEqual(325, len(self.puzzle.solve(
            self.five_starts_five_ends_max_connections)))

    def test_solve_the_witness_seven_starts_six_ends(self):
        self.assertEqual(450, len(self.puzzle.solve(
            self.the_witness_seven_starts_six_ends)))
