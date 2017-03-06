#!/usr/bin/python3

from puzzle import *
import unittest


class TestPuzzle(unittest.TestCase):
    def setUp(self):
        self.sample_node = Node(True, 'a', ['b', 'i', 'h'])

    def test_node_has_exit(self):
        self.assertTrue(self.sample_node.has_exit)

    def test_node_get_name(self):
        self.assertEqual('a', self.sample_node.get_name())

    def test_node_get_connected_to(self):
        self.assertEqual(['b', 'i', 'h'], self.sample_node.get_connected_to())

    def test_node_set_connected_to(self):
        self.sample_node.set_connected_to(['f', 'e', 'd'])
        self.assertEqual(['f', 'e', 'd'], self.sample_node.get_connected_to())

    def test_wheel_add_node(self):
        wheel = Wheel()
        wheel.nodes.append(self.sample_node)
        self.assertEqual(['b', 'i', 'h'], wheel.nodes[0].get_connected_to())

    def test_solve(self):
        wheel = Wheel()
        wheel.nodes.append(self.sample_node)
        puzzle = Puzzle()
        self.assertEqual(
            'Nodes: 1. Exits: 6. Unique paths: 702.',
            puzzle.solve(wheel))
