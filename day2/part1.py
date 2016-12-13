#!/usr/bin/python

import sys

class Position:
    """ Holds the position"""
    def __init__(self):
        self.x = 1
        self.y = 1

    def move_up(self):
        if self.y > 0:
            self.y -= 1

    def move_down(self):
        if self.y < 2:
            self.y += 1

    def move_left(self):
        if self.x > 0:
            self.x -= 1

    def move_right(self):
        if self.x < 2:
            self.x += 1

    def __str__(self):
        return str(self.y * 3 + self.x + 1)

def move(position, next_move):
    if next_move == "U":
        position.move_up()
    elif next_move == "R":
        position.move_right()
    elif next_move == "D":
        position.move_down()
    elif next_move == "L":
        position.move_left()
    else:
        raise ValueError('Move unknown: {}'.format(next_move))
    
if len(sys.argv) != 2:
    raise ValueError('Must have the source file as the first argument')

position = Position()
code = []
with open(sys.argv[1], 'rb') as source:
    line = source.readline()
    while line:
        for c in line.strip():
            move(position, c)
        code.append(str(position))
        line = source.readline()
source.close()            
print "Code: {}".format('-'.join(code))


