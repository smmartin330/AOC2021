values = {}

horizontals = []
verticals = []

grid = {}

low_x = 999999
low_y = 999999
high_x = 0
high_y = 0

count = 1

file = open("day5_input.txt")

data = file.readlines()

for value in data:
    pairs = value.split(' -> ')
    pair_one = pairs[0].split(',')
    pair_two = pairs[1].split(',')
    values[count] = {"x1": int(pair_one[0].strip()),
                     "y1": int(pair_one[1].strip()),
                     "x2": int(pair_two[0].strip()),
                     "y2": int(pair_two[1].strip())}
    
    if values[count]["x1"] == values[count]["x2"]:
        verticals.append(count)
    
    if values[count]["y1"] == values[count]["y2"]:
        horizontals.append(count)


    if values[count]["x1"] < low_x:
        low_x = values[count]["x1"]
    if values[count]["x2"] < low_x:
        low_x = values[count]["x2"]
    if values[count]["x1"] > high_x:
        high_x = values[count]["x1"]
    if values[count]["x2"] > high_x:
        high_x = values[count]["x2"]    

    if values[count]["y1"] < low_y:
        low_y = values[count]["y1"]
    if values[count]["y2"] < low_y:
        low_y = values[count]["y2"]
    if values[count]["y1"] > high_y:
        high_y = values[count]["y1"]
    if values[count]["y2"] > high_y:
        high_y = values[count]["y2"]
    
    count += 1  

for y in range(low_y,high_y+1):
    grid[y] = {}
    for x in range(low_x,high_x+1):
        grid[y][x] = 0

for h_line in horizontals:
    if values[h_line]["x1"] < values[h_line]["x2"]:
        for x in range(values[h_line]["x1"],values[h_line]["x2"]+1):
            grid[values[h_line]["y1"]][x] += 1

    elif values[h_line]["x1"] > values[h_line]["x2"]:
        for x in range(values[h_line]["x2"],values[h_line]["x1"]+1):
            grid[values[h_line]["y1"]][x] += 1

for v_line in verticals:
    if values[v_line]["y1"] < values[v_line]["y2"]:
        for y in range(values[v_line]["y1"],values[v_line]["y2"]+1):
            grid[y][values[v_line]["x1"]] += 1

    elif values[v_line]["y1"] > values[v_line]["y2"]:
        for y in range(values[v_line]["y2"],values[v_line]["y1"]+1):
            grid[y][values[v_line]["x1"]] += 1

#print(horizontals)
#print(verticals)

total = 0
for y in range(low_y,high_y+1):
    for x in range(low_x,high_x+1):
        if grid[y][x] >= 2:
            total += 1
        print(grid[y][x],end='')
    print()

print(total)


