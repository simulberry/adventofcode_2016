import sys

if len(sys.argv) != 2:
    raise ValueError('Must have the source file as the first argument')

class Disk:
    def __init__(self, nb_positions, init_position):
        self.nb_positions = nb_positions
        self.init_position = init_position

    def is_0_position_in(self, time):
        return self.position_in(time) == 0

    def position_in(self, time):
        return (self.init_position + time) % self.nb_positions

    def next_0_position(self, time):
        return time + (self.nb_positions - ((self.init_position + time) % self.nb_positions))
        
class Sculpture:
    def __init__(self, disks):
        self.disks = disks
        self.master_index = 0
        index = 0
        master_nb_positions = 0
        for disk in disks:
            if disk.nb_positions > master_nb_positions:
                self.master_index = index
                master_nb_positions = disk.nb_positions
            index += 1

    def can_drop_at(self, time):
        future_time = time +1
        for disk in self.disks:
            if not disk.is_0_position_in(future_time):
                return False
            future_time += 1
        return True

    def position_in(self, time):
        result = "Time {}:".format(time)
        index = 0
        for disk in self.disks:
            result += "disk {}, position {}; ".format(index, disk.position_in(time))
            index += 1
        return result

    def next_master_0_position_time(self, time):
        return self.disks[self.master_index].next_0_position(time + self.master_index + 1)

    def next_time_to_drop_for_master(self, time):
        drop_time = self.next_master_0_position_time(time) - (self.master_index + 1)
        if drop_time > time:
            return drop_time
        else:
            self.next_master_0_position_time(time + self.master_index)

def get_disk_for_line(line):
    positions = int(line.split(";")[0].split(" ")[3])
    position =  int(line.split(" ")[-1][:-1])
    return Disk(positions, position)

disks = []
with open(sys.argv[1], 'rb') as source:
    line = source.readline()
    while line:
        disks.append(get_disk_for_line(line.strip()))
        line = source.readline()
source.close()

sculpture = Sculpture(disks)
print "Master {}".format(sculpture.master_index)
for x in range(0, 35):
    print "Time {}, is init {}, position {}, next {}".format(x, disks[2].is_0_position_in(x), disks[2].position_in(x), disks[2].next_0_position(x))
    print "Sculpture next master index {}, drop time {}".format(sculpture.next_master_0_position_time(x), sculpture.next_time_to_drop_for_master(x))

time = 0
found = False
index = 0
#print master_index
while not found:
    time = sculpture.next_time_to_drop_for_master(time)
    found = sculpture.can_drop_at(time)
    print "Drop {}".format(sculpture.position_in(time))
    if index > 10:
        found = True

print "Drop in: {}".format(time)
