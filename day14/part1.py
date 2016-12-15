import hashlib
import sys
import re

if len(sys.argv) != 2:
    raise ValueError('Salt is required')

processed = {}
def get_hash(source):
    if not source in processed:
        processed[source] = hashlib.md5(source).hexdigest()
    return processed[source]


index=-1
found_keys = 0
salt = 0
regex = r"(\w)\1{2,}"

while index == -1:
    test_string = get_hash("{}{}".format(sys.argv[1],salt))
    matches = re.findall(regex, test_string)
    if len(matches) > 0:
        regex2 = "({})\\1{{4,}}".format(matches[0][0])
        for x in range(salt+1, salt+1001):
            test_string = get_hash("{}{}".format(sys.argv[1],x))
            sub_matches = re.findall(regex2, test_string)
            if len(sub_matches) > 0:
                found_keys += 1
                if found_keys == 64:
                    index=salt
                    break
    salt += 1
print "Index :{}".format(index) 
        
        
