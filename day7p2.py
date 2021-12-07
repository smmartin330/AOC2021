#this works with the sample data but NOT the real input???? lol math is hard

from statistics import *
from math import *

file = open("day7_sample.txt")
data = []

raw_data = file.readline().strip().split(',')

for x in raw_data:
    data.append(int(x))

rounded_mean_pos = round(mean(data))

total = 0

def tri(x):
    return ((x**2)+x)/2

for x in data:
    if x > rounded_mean_pos:
        total += tri(x - rounded_mean_pos)
    elif x < rounded_mean_pos:
        total += tri(rounded_mean_pos - x)
    elif x == rounded_mean_pos:
        pass

print(total)
