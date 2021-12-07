# my dataset needed the floored mean, the sample dataset needed the rounded mean. i love math. 

from statistics import *
from math import *

file = open("day7_input.txt")
data = []

raw_data = file.readline().strip().split(',')

for x in raw_data:
    data.append(int(x))

median_pos = median(data)
rounded_mean_pos = round(mean(data))
floored_mean_pos = floor(mean(data))
print(f"Median: {median_pos}")
print(f"Mean: {mean(data)}")
print(f"Rounded Mean: {rounded_mean_pos}")
print(f"Smallest value: {min(data)}")
print(f"largest value: {max(data)}")
total = 0

def tri(x):
    return ((x**2)+x)/2

for x in data:
    if x > floored_mean_pos:
        #print(f"Moving {x - rounded_mean_pos} at cost {tri(x - rounded_mean_pos)}")
        total += tri(x - floored_mean_pos)
    elif x < floored_mean_pos:
        #print(f"Moving {x - rounded_mean_pos} at cost {tri(x - rounded_mean_pos)}")
        total += tri(floored_mean_pos - x)
    elif x == floored_mean_pos:
        #print(f"Moving {x - rounded_mean_pos} at cost {tri(x - rounded_mean_pos)}")
        pass

print(total)
