import hashlib
import sys
import collections

if len(sys.argv) != 2:
    raise ValueError('Input file is required')

letter_count = []
with open(sys.argv[1], 'rb') as source:
    line = source.readline()
    while line:
        index = 0
    	for letter in line.strip():
	    if len(letter_count) < index + 1:
	       letter_count.append({})
	    if letter in letter_count[index]:
                letter_count[index][letter] += 1
            else:
                letter_count[index][letter] = 1
	    index += 1
        line = source.readline()
source.close()            

message = ""
for column in letter_count:
    ordered = collections.OrderedDict(sorted(column.items(), key=lambda t :t[1], reverse=True))
    message += ordered.items()[0][0]

print "Message: {}".format(message)
