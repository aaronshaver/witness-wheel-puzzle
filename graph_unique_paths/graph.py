#!/usr/bin/python3

import json


def _get_nodes(graph, boolean_condition):
    nodes = []
    for node, metadata in graph["graph"]["nodes"][0].items():
        if metadata[boolean_condition]:
            nodes.append(node)
    return nodes


def _find_all_paths(graph, start_node, end_node, path=None):
    if path is None:
        path = []
    path = path + [start_node]
    if start_node == end_node:
        return [path]  # doing [] is necessary for graphs with a "cycle"
    connection_paths = []
    for node, metadata in graph["graph"]["nodes"][0].items():
        if node == start_node:
            for connection in metadata['connections']:
                if connection not in path:
                    new_paths = _find_all_paths(graph, connection, end_node,
                                               path)
                    for new_path in new_paths:
                        connection_paths.append(new_path)
    return connection_paths


def _get_json_string(path):
    with open(path) as file:
        json_file = file.read()
        return json.loads(json_file)


def solve(json_file_path):
    graph = _get_json_string(json_file_path) 
    start_nodes = _get_nodes(graph, 'is_start_node')
    end_nodes = _get_nodes(graph, 'is_end_node')

    for end_node in end_nodes:
        for start_node in start_nodes:
            temp_paths = _find_all_paths(graph, start_node, end_node)
            final_paths = []
            for path in temp_paths:  # undo nesting caused by 'return [path]'
                final_paths.append(path)
    return final_paths

