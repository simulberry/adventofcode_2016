#!/usr/bin/python

import sys

class Position:
    """ Holds the position"""
    
    def __init__(self):
        self.x = -2
        self.y = 0

    @staticmethod
    def _is_valid(x, y):
        return abs(x) + abs(y) <= 2
    
    def move_up(self):
        if Position._is_valid(self.x, self.y+1):
            self.y += 1

    def move_down(self):
        if Position._is_valid(self.x, self.y-1):
            self.y -= 1

    def move_left(self):
        if Position._is_valid(self.x-1, self.y):
            self.x -= 1

    def move_right(self):
        if Position._is_valid(self.x+1, self.y):
            self.x += 1

    def __str__(self):
        value = 0
        for y in range(2, -3, -1):
            for x in range(-2, 3, 1):
                if Position._is_valid(x, y):
                    value += 1
                if x == self.x and y == self.y:
                    if value < 10:
                        return str(value)
                    else:
                        return str(chr(value - 10 + 65))

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


