""" Calculates max unique paths for directed graphs that have start and end nodes """
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
        return [path]
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
    """ Solves/calculates all unique paths for direct graphs with start, end nodes

    Args:
        json_file_path (str): path to .json file which contains graph nodes

    Returns:
        list: A list of lists of all the unique paths for the graph
    """
    graph = _get_json_string(json_file_path)
    start_nodes = _get_nodes(graph, 'is_start_node')
    end_nodes = _get_nodes(graph, 'is_end_node')
    all_paths = []

    for end_node in end_nodes:
        for start_node in start_nodes:
            all_paths.append(_find_all_paths(graph, start_node, end_node))

    flattened_list = [unique_path for sublist in all_paths for unique_path in sublist]
    return flattened_list
