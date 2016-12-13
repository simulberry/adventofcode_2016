#!/usr/bin/python

import sys
import collections

class Room:
    def __init__(self, encoded):
        splited = encoded.split('[')
        self.checksum = splited[1][:-1]
        self.letters = filter(lambda x: x.isalpha(), splited[0])
        self.sector_id = int(filter(lambda x: x.isdigit(), splited[0]))
    def is_valid(self):
        letters_count = {}
        for letter in self.letters:
            if not letter in letters_count:
                letters_count[letter] = 1
            else:
                letters_count[letter] +=1
        sorted_letters = collections.OrderedDict(sorted(letters_count.items(), key=lambda t :t[1], reverse=True))

        for checksum_char in self.checksum:
            current_count = sorted_letters.items()[0][1]
            if checksum_char not in sorted_letters or sorted_letters[checksum_char] != current_count:
                return False
            del sorted_letters[checksum_char]
        return True

    def __str__(self):
        return "letters: {}, checksum: {}, sector: {}, is_valid:{}".format(self.letters, self.checksum, self.sector_id, self.is_valid())

if len(sys.argv) != 2:
    raise ValueError('Must have the source file as the first argument')

sum_sector_ids = 0
with open(sys.argv[1], 'rb') as source:
    line = source.readline()
    while line:
        room = Room(line.strip())
        if(room.is_valid()):
            sum_sector_ids +=room.sector_id
        line = source.readline()
source.close()            
print "Sum sector Ids: {}".format(sum_sector_ids)


