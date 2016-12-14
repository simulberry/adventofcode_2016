import hashlib
import sys

if len(sys.argv) != 2:
    raise ValueError('Door ID is required')

password = ""
current_index = 0
while len(password)<8:
    to_hash = "{}{}".format(sys.argv[1], current_index)
    value = hashlib.md5(to_hash).hexdigest()
    if value[:5] == "00000":
        print "unencoded {}, index {}, found {}, value {}".format(to_hash, current_index, value, value[5:6])
        password += value[5:6]
    current_index += 1

print "password: {}".format(password)
