#!/usr/bin/python3


def get_end_nodes(graph):
    exits = []
    for root_node, connected_nodes in graph.items():
        for node in connected_nodes:
            if 'Exit' in node:
                exits.append(node)
    return exits


def find_all_paths(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def solve(graph):
    if graph is None:
        raise TypeError
    unique_paths = []
    for exit in get_end_nodes(graph):
        for start, connected_nodes in graph.items():
            unique_paths += find_all_paths(graph, start, exit)
    return unique_paths
