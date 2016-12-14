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

def get_new_locations(maze, current, visited, current_count, max_distance):
    if current_count==max_distance:
        return [current]

    new_visited=list(visited)
    new_visited.append(current)
    moves = maze.avaliable_moves(current[0], current[1])

    all_locations = [current]
    for move in moves:
        if move not in new_visited:
            locations = get_new_locations(maze, move, new_visited, current_count + 1, max_distance)
            for location in locations:
                if not location in all_locations:
                    all_locations.append(location)
    return all_locations

final_locations = get_new_locations(maze, (1,1), [], 0, 50)
print "Locations :{}".format(len(final_locations))
    

