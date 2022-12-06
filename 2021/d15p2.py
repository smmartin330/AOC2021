import d15data

cavern = []
tentative = []
distance = []
unvisited = set()
paths = []
distanced = []

for line in d15data.my.split('\n'):
    rooms = [int(char) for char in line]
    
    for inc in range(1,5):
        for char in line:
            new_char = int(char) + inc
            if new_char > 9:
                new_char -= 9
            rooms.append(new_char)
    
    cavern.append(rooms)

cavern_start = cavern.copy()
for i in range(1,5):
    for row in cavern_start:
        new_row = []    
        for room in row:
            new_room = room + i
            if new_room > 9:
                new_room -= 9
            new_row.append(new_room)
        cavern.append(new_row)
    
for y in range(0,len(cavern)):
    distance.append([])
    for x in range(0,len(cavern)):
        unvisited.add((x,y))
        distance[y].append(99999)
    
unvisited.remove((0,0))
distance[0][0] = 0
node = [0,0]
destination = [len(cavern)-1,len(cavern)-1]
done = False

while done == False: 

    neighbors = []
    
    x,y = node
    if (x-1,y) in unvisited:
        neighbors.append([x-1,y])
    
    if (x+1,y) in unvisited:
        neighbors.append([x+1,y])
    
    if (x,y-1) in unvisited:
        neighbors.append([x,y-1])
        
    if (x,y+1) in unvisited:
        neighbors.append([x,y+1])
    
    this_x,this_y = node
    for neighbor in neighbors:
        neighbor_x,neighbor_y = neighbor
     
        tentative_distance = distance[this_y][this_x] + cavern[neighbor_y][neighbor_x]
        if distance[neighbor_y][neighbor_x] > tentative_distance:
            distance[neighbor_y][neighbor_x] = tentative_distance
            distanced.append([neighbor_x,neighbor_y])
        
    try:
        unvisited.remove((node[0],node[1]))
    except:
        pass
    tentative_distance = 99999
    next_node = []
    
    for candidate in distanced:
        x,y = candidate
        if (candidate[0],candidate[1]) in unvisited:
            if distance[y][x] < tentative_distance:
                tentative_distance = distance[y][x]
                next_node = [x,y]
    
    #print(next_node)
    try:
        distanced.remove(next_node)

        node = next_node
    except:
        pass
    
    if len(unvisited) == 0:
        done = True
    print(len(unvisited))

print(distance[destination[1]][destination[0]])
