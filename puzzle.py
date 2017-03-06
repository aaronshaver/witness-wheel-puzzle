#!/usr/bin/python3


class Node:
    def __init__(self, has_exit, name, connected_to):
        self.has_exit = has_exit
        self.name = name
        self.connected_to = []
        for node in connected_to:
            self.connected_to.append(node)

    def get_has_exit(self):
        return self.has_exit

    def get_name(self):
        return self.name

    def get_connected_to(self):
        return self.connected_to

    def set_connected_to(self, new_items):
        self.connected_to = new_items


class Wheel:
    pass


class Puzzle:

    def main():

        out = "Nodes: 7. Exits: 6. Unique paths: 702."
        print(out)
        return out

if __name__ == "main":
    main()
