import hashlib
import sys

if len(sys.argv) != 2:
    raise ValueError('Door ID is required')

password_list = [-1] * 8
current_index = 0
while len(filter(lambda x: x == -1, password_list)) > 0:
    to_hash = "{}{}".format(sys.argv[1], current_index)
    value = hashlib.md5(to_hash).hexdigest()
    if value[:5] == "00000":
        position = value[5:6]
        if position.isdigit() and int(position)<8 and password_list[int(position)] == -1:
            password_value = value[6:7]
            print "unencoded {}, index {}, found {}, value {}, position {}".format(to_hash, current_index, value, password_value, position)
            password_list[int(position)] = password_value
    current_index += 1

print "password: {}".format(''.join(str(x) for x in password_list))
