import d15data

cavern = []
tentative = []
distance = []
unvisited = []
paths = []

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
        unvisited.append([x,y])
        distance[y].append(99999)
    
distance[0][0] = 0
node = [0,0]
destination = [len(cavern)-1,len(cavern)-1]
done = False
print(destination)
while done == False: 

    neighbors = []
    
    x,y = node
    if [x-1,y] in unvisited:
        neighbors.append([x-1,y])
    
    if [x+1,y] in unvisited:
        neighbors.append([x+1,y])
    
    if [x,y-1] in unvisited:
        neighbors.append([x,y-1])
        
    if [x,y+1] in unvisited:
        neighbors.append([x,y+1])
    
    this_x,this_y = node
    for neighbor in neighbors:
        neighbor_x,neighbor_y = neighbor
     
        tentative_distance = distance[this_y][this_x] + cavern[neighbor_y][neighbor_x]
        if distance[neighbor_y][neighbor_x] > tentative_distance:
            distance[neighbor_y][neighbor_x] = tentative_distance
        
    unvisited.remove(node)
    tentative_distance = 99999
    next_node = []
    
    for candidate in unvisited:
        x,y = candidate
        if distance[y][x] < tentative_distance:
            tentative_distance = distance[y][x]
            next_node = candidate
    
    node = next_node
    if unvisited == []:
        done = True
    print(len(unvisited))

print(distance[destination[1]][destination[0]])
