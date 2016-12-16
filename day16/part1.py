import sys
import re
from string import maketrans

if len(sys.argv) != 3:
    raise ValueError('Must have the input and length')

def get_checksum(source):
    index = 0
    checksum = ""
    regex = r"((0){2})|((1){2})"
    end = len(source)-1
    while index < end:
        checksum += str(len(re.findall(regex, source[index: index+2])))
        index += 2
    return checksum

def reverse_chars(source):
    return source.translate(maketrans("10","01"))

data = sys.argv[1]
length = int(sys.argv[2])
while len(data) < length:
    data += "{}{}".format("0", reverse_chars(data[::-1]))
data = data[0:length]
print "Data: {}".format(data)

checksum = get_checksum(data)
while len(checksum) % 2 == 0:
    checksum = get_checksum(checksum)

print "Checksum: {}".format(checksum)
