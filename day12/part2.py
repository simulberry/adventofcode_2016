import sys

if len(sys.argv) != 2:
    raise ValueError('Must have the source file as the first argument')

class Processor:

    def __init__(self):
        self.registry = [0] * 4

    def get_registry_index(self, reg):
        return ord(reg)-97

    def execute(self, instruction):
        instruction_parts = instruction.split(' ')
        if instruction_parts[0] == "cpy":
            if instruction_parts[1].isdigit():
                self.registry[self.get_registry_index(instruction_parts[2])] = int(instruction_parts[1])
            else:
                self.registry[self.get_registry_index(instruction_parts[2])] =  self.registry[self.get_registry_index(instruction_parts[1])]
        elif instruction_parts[0] == "inc":
            self.registry[self.get_registry_index(instruction_parts[1])] += 1
        elif instruction_parts[0] == "dec":
            self.registry[self.get_registry_index(instruction_parts[1])] -= 1
        elif instruction_parts[0] == "jnz" :
            should_execute = False
            if instruction_parts[1].isdigit() and int(instruction_parts[1]) != 0:
                should_execute = True
            elif self.registry[self.get_registry_index(instruction_parts[1])] != 0:
                should_execute = True
            if should_execute:
                return int(instruction_parts[2])
        return 0

    def __str__(self):
        return "a {}, b {}, c {}, d {}".format(self.registry[0], self.registry[1], self.registry[2], self.registry[3])
    def execute_program(self, instructions):
        execution_index = 0
        while execution_index < len(instructions):
#            print "executing index {}, instruction {}, status {}".format(execution_index, instructions[execution_index].strip(), str(processor))
            jump = self.execute(instructions[execution_index].strip())
            if(jump != 0):
                execution_index += jump
            else:
                execution_index += 1

processor = Processor()
processor.registry[2] = 1
with open(sys.argv[1], 'rb') as source:
    lines = source.readlines()
    processor.execute_program(lines)
source.close()
print "Value of a: {}".format(processor.registry[0])



