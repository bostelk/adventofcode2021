"""
DAY 2
PART 1
"""
import sys
import re
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    depth = 0
    horizontal = 0
    while line:
        parts = line.split(" ")
        if parts[0] == "forward":
            horizontal += int(parts[1])
        elif parts[0] == "up":
            depth -= int(parts[1])
        elif parts[0] == "down":
            depth += int(parts[1])
        line = file.readline()
    print("End of input")
    product = horizontal * depth
    print("%s * %s = %s" % (horizontal, depth, product))
