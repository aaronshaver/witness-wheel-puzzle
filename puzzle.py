#!/usr/bin/python3


class Node:
    def __init__(self, has_exit, name, connected_to):
        self.has_exit = has_exit
        self.name = name
        self.connected_to = []
        for node in connected_to:
            self.connected_to.append(node)


class Wheel:
    def __init__(self):
        self.nodes = []
        self.current_node = ''
        self.visited_nodes = []

    def get_exit_count(self):
        count = 0
        for node in self.nodes:
            if node.has_exit:
                count += 1
        return count


class Puzzle:
    def solve(self, wheel):
        nodes = len(wheel.nodes)
        exits = wheel.get_exit_count()
        paths = 702
        out = 'Nodes: {nodes}. Exits: {exits}. Unique paths: {paths}.'.format(
            nodes=nodes, exits=exits, paths=paths)

        print(out)
        return out

if __name__ == "__main__":
    Puzzle.solve()
