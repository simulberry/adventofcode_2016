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

    def get_location(self):
        return "x:{}, y:{}".format(self.x, self.y)

    def distance(self, x = 0, y = 0):
        return abs(self.x - x) + abs(self.y - y)
        
if len(sys.argv) != 2:
    raise ValueError('Must have the source file as the first argument')

position = Position()
position_history = {position.get_location(): 1}
hq_x = 0
hq_y = 0
hq_found = False


# move_code: format [L|R]XXX
# L & R are the rotation before the move
# XXX is the number of blocks to move
def move(position, move_code):
    global position_history
    global hq_x
    global hq_y
    global hq_found
    rotation = move_code[:1]
    if rotation == "R":
        position.rotate_right()
    elif rotation == "L":
        position.rotate_left()
    else:
        raise ValueError('Unknown rotation {}'.format(rotation))
    if not hq_found:
        for x in range(0, int(move_code[1:])):
            position.move_forward(1)
            if not hq_found:
                if position.get_location() in position_history:
                    hq_x = position.x
                    hq_y = position.y
                    hq_found = True
                else:
                    position_history[position.get_location()] = 1
    else: # When found there is no need to move one by one
        position.move_forward(int(move_code[1:]))

with open(sys.argv[1], 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        for element in row:
            move(position, element.strip())
csvfile.close()
print "Final position: {}".format(position)
print "Distance from the start: {}".format(position.distance())
start_position = Position()
print "Distance from HQ: {}".format(start_position.distance(hq_x, hq_y))
