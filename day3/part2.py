#!/usr/bin/python

import sys
import csv

class Triangle:
    """ Holds the position"""
    
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        return (self.a + self.b) > self.c and (self.b + self.c) > self.a and (self.a + self.c) > self.b 

    def __str__(self):
        return "a: {}, b: {}, c: {}".format(self.a, self.b, self.c)

if len(sys.argv) != 2:
    raise ValueError('Must have the source file as the first argument')

valid = 0
with open(sys.argv[1], 'rb') as source:
    line = source.readline()
    values = []
    while line:
        values.append(int(line[2:5]))
        values.append(int(line[7:10]))
        values.append(int(line[12:16]))
        #triangle = Triangle(a=int(line[2:5]), b=int(line[7:10]), c=int(line[12:16]))
        if(len(values) == 9):
            for x in range(0,3):
                triangle = Triangle(a=values[x], b=values[x+3], c=values[x+6])
                if triangle.is_valid():
                    valid += 1
            values = []
        line = source.readline()
source.close()            
print "Valid triangles: {}".format(valid)


