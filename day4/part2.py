#!/usr/bin/python

import sys
import collections

class Room:
    def __init__(self, encoded):
        splited = encoded.split('[')
        self.checksum = splited[1][:-1]
        self.letters = filter(lambda x: x.isalpha(), splited[0])
        self.sector_id = int(filter(lambda x: x.isdigit(), splited[0]))
        self.encoded_name = splited[0]

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

    def decode(self):
        if not self.is_valid():
            raise ValueError('Cannot decrypt')
        decoded = ""
        for letter in self.encoded_name:
            if letter == "-":
                decoded += " "
            elif letter.isalpha():
                letter_number = ord(letter) - 97
                letter_number += self.sector_id
                decoded += chr(letter_number % 26 + 97)
        return decoded
        
    def __str__(self):
        return "letters: {}, checksum: {}, sector: {}, is_valid:{}".format(self.letters, self.checksum, self.sector_id, self.is_valid())

if len(sys.argv) != 3:
    raise ValueError('Must have the source file as the first argument and the room name as the second argument')

room = None
with open(sys.argv[1], 'rb') as source:
    line = source.readline()
    while line:
        room = Room(line.strip())
        if room.is_valid() and sys.argv[2].upper() in room.decode().upper():
            room = room
            break
        line = source.readline()
source.close()            
print "Room sector: {}, room name: {}".format(room.sector_id, room.decode())


