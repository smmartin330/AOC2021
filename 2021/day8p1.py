#unique lengths
unique = { 1 : 2, 4: 4,  7: 3, 8: 7}

#shared lengths
lengths = [ 0, 0, 1, 1, 1, 3, 3, 1 ]

#standard
# 1 
standard =  { 0: ["a", "b", "c", "e", "f", "g"],
              1: ["c", "f"],
              2: ["a", "c", "d", "e", "g"],
              3: ["a", "c", "d", "f", "g"],
              4: ["b", "c", "d", "f"],
              5: ["a", "b", "d", "f", "g"],
              6: ["a", "b", "d", "e", "f", "g"],
              7: ["a", "c", "f"],
              8: ["a", "b", "c", "d", "e", "f", "g"],
              9: ["a", "b", "c", "d", "f", "g"] 
}

signal = []
output = []
line_count = 0

file = open("day8_input.txt")

contents = file.readlines()

for line in contents:
    signal.append(line.split('|')[0].strip())
    output.append(line.split('|')[1].strip())
    line_count += 1

unique_count = 0
for o in output:

    for v in o.split():
        if len(v) in [2, 4, 3, 7]:
            unique_count += 1

print(unique_count)
