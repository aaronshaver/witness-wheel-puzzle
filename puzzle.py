#!/usr/bin/python3


class Puzzle:
    def get_all_exits(self, graph):
        exits = []
        for root_node, connected_nodes in graph.items():
            for node in connected_nodes:
                if 'Exit' in node:
                    exits.append(node)
        return exits

    def find_all_paths(self, graph, start, end, path=None):
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
                newpaths = self.find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def solve(self, graph=None):
        unique_paths = []
        for exit in self.get_all_exits(graph):
            for start, connected_nodes in graph.items():
                unique_paths += self.find_all_paths(graph, start, exit)
        return unique_paths
