#!/usr/bin/python3

import graph_unique_paths
import unittest

graph = graph_unique_paths


class TestPuzzle(unittest.TestCase):
    folder = 'json/'
    ext = '.json'
   
    def test_solve_1_start_1_end(self):
        test_data = self.folder + '1_start_1_end' + self.ext
        self.assertEqual(1, len(graph.solve(test_data)))

    def test_solve_1_start_2_end(self):
        test_data = self.folder + '1_start_2_end' + self.ext
        self.assertEqual(2, len(graph.solve(test_data)))

    def test_solve_2_start_1_end(self):
        test_data = self.folder + '2_start_1_end' + self.ext
        self.assertEqual(2, len(graph.solve(test_data)))

    def test_solve_2_start_2_end(self):
        test_data = self.folder + '2_start_2_end' + self.ext
        self.assertEqual(4, len(graph.solve(test_data)))

    def test_solve_3_start_1_end(self):
        test_data = self.folder + '3_start_1_end' + self.ext
        self.assertEqual(5, len(graph.solve(test_data)))

    def test_solve_7_start_6_end(self):
        test_data = self.folder + '7_start_6_end' + self.ext
        self.assertEqual(642, len(graph.solve(test_data)))

    def test_solve_4_start_4_end_max_connections(self):
        test_data = self.folder + '4_start_4_end_max_connections' + self.ext
        self.assertEqual(64, len(graph.solve(test_data)))
