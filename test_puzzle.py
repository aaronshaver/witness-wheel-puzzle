#!/usr/bin/python3

from puzzle import *
import unittest


class TestPuzzle(unittest.TestCase):

    def setUp(self):
        self.node = Node(True, 'a', ['b', 'i', 'h'])

    def test_node_has_exit(self):
        self.assertTrue(self.node.get_has_exit())

    def test_node_get_name(self):
        self.assertEqual('a', self.node.get_name())

    def test_node_get_connected_to(self):
        self.assertEqual(['b', 'i', 'h'], self.node.get_connected_to())

    def test_node_set_connected_to(self):
        self.node.set_connected_to(['f', 'e', 'd'])
        self.assertEqual(['f', 'e', 'd'], self.node.get_connected_to())

    def test_main(self):
        self.assertEqual(
            'Nodes: 7. Exits: 6. Unique paths: 702.',
            Puzzle.main())
