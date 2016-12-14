import sys

if len(sys.argv) != 4:
    raise ValueError('Favorite number and destination are required')

class Maze:
    def __init__(self, fav_number):
        self.fav_number = fav_number

    def is_wall(self, x, y):
        calculated = x*x + 3*x + 2*x*y + y + y*y + self.fav_number
        in_binary = "{0:b}".format(calculated)
        return in_binary.count('1') % 2 == 1

    def avaliable_moves(self, x, y):
        moves = []
        if x > 0 and not self.is_wall(x-1, y):
            moves.append((x-1, y))
        if y > 0 and not self.is_wall(x, y-1):
            moves.append((x, y-1))
        if not self.is_wall(x+1, y):
            moves.append((x+1, y))
        if not self.is_wall(x, y+1):
            moves.append((x, y+1))
        return moves

maze = Maze(int(sys.argv[1]))

def shorter_path(maze, visited, current, destination, current_count):
    if current[0] == destination[0] and current[1] == destination[1]:
        return current_count
    moves = maze.avaliable_moves(current[0], current[1])
    new_visited = list(visited)
    new_visited.append(current)

    shortest_distance = -1
    for move in moves:
        if not move in visited:
            distance = shorter_path(maze, new_visited, move, destination, current_count + 1)
            if distance > -1:
                if shortest_distance == -1:
                    shortest_distance = distance
                elif distance < shortest_distance:
                    shortest_distance = distance
    return shortest_distance

final_distance = shorter_path(maze, [], (1,1), (int(sys.argv[2]), int(sys.argv[3])), 0)

print "Distance :{}".format(final_distance)
    

