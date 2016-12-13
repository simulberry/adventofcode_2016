#!/usr/bin/python

import sys
import csv

class Triangle:
    """ Holds the position"""
    
    def __init__(self, a, b, c):
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
    while line:
        triangle = Triangle(a=int(line[2:5]), b=int(line[7:10]), c=int(line[12:16]))
        if triangle.is_valid():
            valid += 1
        line = source.readline()
source.close()            
print "Valid triangles: {}".format(valid)


