#!/usr/bin/python3

import graph_unique_paths
import unittest

graph = graph_unique_paths


class TestPuzzle(unittest.TestCase):
    def test_solve_1_start_1_end(self):
        with open('json/1_start_1_end.json', 'r') as file:
            json_graph = file.read()
        self.assertEqual(1, len(graph.solve(json_graph)))

    def test_solve_1_start_2_end(self):
        with open('json/1_start_2_end.json', 'r') as file:
            json_graph = file.read()
        self.assertEqual(2, len(graph.solve(json_graph)))

    def test_solve_2_start_1_end(self):
        with open('json/2_start_1_end.json', 'r') as file:
            json_graph = file.read()
        self.assertEqual(2, len(graph.solve(json_graph)))

    def test_solve_2_start_2_end(self):
        with open('json/2_start_2_end.json', 'r') as file:
            json_graph = file.read()
        self.assertEqual(4, len(graph.solve(json_graph)))

    def test_solve_3_start_1_end(self):
        with open('json/3_start_1_end.json', 'r') as file:
            json_graph = file.read()
        self.assertEqual(5, len(graph.solve(json_graph)))

    def test_solve_7_start_6_end(self):
        with open('json/7_start_6_end.json', 'r') as file:
            json_graph = file.read()
        self.assertEqual(642, len(graph.solve(json_graph)))
