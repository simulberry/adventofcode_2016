#!/usr/bin/python

import sys
import csv

# Orientations
#        North = 1
#        East = 2
#        South = 3
#        West = 4
                    
class Position:
    """ Holds the position and facing direction """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.orientation = 1

    def rotate_right(self):
        if self.orientation == 4:
            self.orientation = 1;
        else:
            self.orientation += 1
        
    def rotate_left(self):
        if self.orientation == 1:
            self.orientation = 4;
        else:
            self.orientation -= 1

    def move_forward(self, block):
        if self.orientation % 2 == 0:
            # east or west (x axe)
            self.x += block if self.orientation == 2 else block * - 1
        else:
            self.y += block if self.orientation == 1 else block * - 1

    def __str__(self):
        return "x:{}, y:{}, facing:{}".format(self.x, self.y, self.orientation)

    # move_code: format [L|R]XXX
    # L & R are the rotation before the move
    # XXX is the number of blocks to move
    def move(self, move_code):
        rotation = move_code[:1]
        if rotation == "R":
            self.rotate_right()
        elif rotation == "L":
           self.rotate_left()
        else:
            raise ValueError('Unknown rotation {}'.format(rotation))
        self.move_forward(int(move_code[1:]))

if len(sys.argv) != 2:
    ValueError('Must have the source file as the first argument')

position = Position()
with open(sys.argv[1], 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        for element in row:
            position.move(element.strip())

print "Final position: {}".format(position)
print "Distance from the start: {}".format(abs(position.x) + abs(position.y))


