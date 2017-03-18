# graph-unique-paths

## Usage

### Module

Example of how to use the module:

    import graph_unique_paths as g
    g.solve('json/1_start_1_end.json')

It accepts a path to a .json file and returns a list of all the unique paths given the requirement that one start on a start node and finish on an end node.

### Tests

To run the tests: ``python -m unittest discover``

## Description

This program calculates the maximum unique paths for directed graphs which have start and
end nodes (you must start on a start node, and end on an end node). I was
originally inspired by wanting to know how many permutations the "wheel" puzzles
from the game The Witness had (the ones in the desert area). But this module is
sufficiently flexible that you can use it on other types of graphs too.

The Witness puzzles have 7 normal nodes (which all act as starting points), and
6 of those nodes have "end" nodes attached to the outside of them (where your
path finishes and you're unable to draw anymore).

You can't revisit or pass through a node if you've been on it in the past. There
are 12 normal vertices in the puzzle. If you count the edge normal nodes
connecting to the end nodes, there are 18 vertices.

End nodes are special: you can't start on an end node, and you must finish on
one.

Here's my attempt to draw an ASCII version of the puzzle (end nodes not shown):

                           +------+
                           |      |
                           |      |X
                        XXX+------+XXXXX
                    XXXX      X         XXXXX
               XXXXXX         X             XXXX
    +------+XXXX              X                XXXXX+-------+
    |      |                  X                     |       |
    |      |                  X                     |       |
    +------+XX                X                XXXXX|       |
        X    XXXXX         +--------+    XXXXXXX    +-------+
        X        XXXXX     |        |XXXXX               X
        X            XXXXXX|        |                    X
       X               XXX |        |X                   X
       X           XXXX    +--------+XXXXX               X
       X        XXXX            X        XXXX            X
       X      XXX               X           XXX          X
       X    XXX                 X             XXXXX      X
     +-------+                  X                 XXXX   X
     |       |                  X                    +-------+
     |       |                 XX                    |       |
     |       |                  X                    |       |
     +-------+XXX               X                    |       |
                XXXXXX          X                XXXX+-------+
                     XXX     +-------+      XXXXXX
                       XXXXX |       |  XXXXX
                           X |       |
                             |       |
                             +-------+

If that diagram doesn't make sense, try this URL, which has screenshots from the
game: http://www.ign.com/wikis/the-witness/Desert_Ruins
