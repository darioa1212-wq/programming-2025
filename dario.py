# AOC DAY 1
# Author: Dario
# 1 December

def part_one():
    cur_location = 50

   # read every line in the instructions
    with open("data/aoc-2025-day1.txt") as file:
        for line in file:
            direction = line[0]
            distance = int(line[1:])
            print(direction, distance)

            if direction == 'R':
                cur_location += distance
            else:
                cur_location -= distance
            #  if we land on zero keep track of it
        print(cur_location)
        # print how many times we land on zero



if __name__ == "__main__":
    part_one()
