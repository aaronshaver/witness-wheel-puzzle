#!/usr/bin/python3


class Puzzle:
    def get_all_exits(self, graph):
        exits = []
        for key, value in graph.items():
            for item in value:
                if 'Exit' in item:
                    exits += key
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
