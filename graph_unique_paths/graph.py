#!/usr/bin/python3

import json
from pprint import pprint


def get_nodes(graph, boolean_condition):
    nodes = []
    for node, metadata in graph["graph"]["nodes"][0].items():
        if metadata[boolean_condition]:
            nodes.append(node)
    return nodes


def find_all_paths(graph, start_node, end_node, path=None):
    if path is None:
        path = []
    path = path + [start_node]
    if start_node == end_node:
        return [path]  # doing [] is necessary for graphs with "cycle"
    connection_paths = []
    for node, metadata in graph["graph"]["nodes"][0].items():
        if node == start_node:
            for connection in metadata['connections']:
                if connection not in path:
                    new_paths = find_all_paths(graph, connection, end_node,
                                               path)
                    for new_path in new_paths:
                        connection_paths.append(new_path)
    return connection_paths


def solve(json_string):
    graph = json.loads(json_string)
    final_paths = []
    start_nodes = get_nodes(graph, 'is_start_node')
    end_nodes = get_nodes(graph, 'is_end_node')
    for end_node in end_nodes:
        for start_node in start_nodes:
            temp_paths = find_all_paths(graph, start_node, end_node)
            for path in temp_paths:  # undo nesting caused by 'return [path]'
                final_paths.append(path)
    return final_paths
