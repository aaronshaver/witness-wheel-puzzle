# witness-wheel-puzzle

## Description

This program calculates the maximum unique paths for the 7-node "wheel" puzzles from the game The Witness.

The puzzles have 7 nodes (which all act as starting points), and 6 of those nodes have "exits" (your path finishes and you're unable to draw anymore). You can't revisit or pass through a node if you've been on it in the past. There are 12 vertices in the puzzle.

I will now attempt to draw an ASCII version of the puzzle:

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

If that diagram doesn't do the trick, try this URL, which has screenshots from the game: http://www.ign.com/wikis/the-witness/Desert_Ruins

## Usage

To run the program: ``python