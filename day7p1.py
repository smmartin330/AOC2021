#this works with both the sample data and the real input

from statistics import *

file = open("day7_input.txt")
data = []

raw_data = file.readline().strip().split(',')

for x in raw_data:
    data.append(int(x))

median_pos = median(data)

total = 0

for x in data:
    if x > median_pos:
        total += (x - median_pos)
    elif x < median_pos:
        total += (median_pos - x)
    elif x == median_pos:
        pass

print(total)
