from day9data import *

datamap = []
checked = []
low_points = []
risk = 0
basin_sizes = []

for row in data.split():
    this_row = []
    bool_row = []
    for x in row:
        bool_row.append(False)
        this_row.append(int(x))
    datamap.append(this_row)
    checked.append(bool_row)
    
height = len(datamap)
width = len(datamap[0])

def get_adjacents(x, y, datamap=datamap, height=height, width=width):
    value = datamap[y][x]
    adj_values = []
    adj_spaces = []        
    try:
        if y - 1 >= 0:
            adj_values.append(datamap[y-1][x])
            adj_spaces.append([x,y-1])
    except:
        pass 
    
    try:
        if y + 1 <= height:
            adj_values.append(datamap[y+1][x])
            adj_spaces.append([x,y+1])
    except:
        pass
        
    try:
        if x - 1 >= 0:
            adj_values.append(datamap[y][x-1])
            adj_spaces.append([x-1,y])
    except:
        pass
    
    try:
        if x+1 <= width:
            adj_values.append(datamap[y][x+1])
            adj_spaces.append([x+1,y])
    except: 
        pass
    
    return value, adj_spaces, adj_values

    
def get_low_points(datamap=datamap, height=height, width=width):
    risk = 0
    for y in range(0,height):
        for x in range(0,width):
            value, adj_spaces, adj_values = get_adjacents(x,y)
            
            if value < min(adj_values):
                low_points.append([x,y,adj_spaces])
                risk += (value + 1)

    return low_points, risk


def get_basin_size(datamap=datamap,checked=checked,low_point=[0,0,[0,0]]):
    new_adjacents = []
    basin_size = 1                                                      # For this starting low point, The basin size starts at one.
    x = low_point[0]                                                    # Get the X of the low point
    y = low_point[1]                                                    # Get the Y of the low point
    adjacents = low_point[2]                                            # Get the adjacents of the low point
    checked[y][x] = True                                                # Mark the low point itself as checked
    while adjacents != [] or new_adjacents != []:
        for new in new_adjacents:
            adjacents.append(new)
        new_adjacents = []
        for adj in reversed(adjacents):                                     # For each point adjacent in the list
            adj_x = adj[0]                                                  # Get the X of the point
            adj_y = adj[1]                                                  # Get the Y of the point
            if datamap[adj_y][adj_x] == 9:                                  # Is it a nine?
                checked[adj_y][adj_x] = True                                # If so, mark it as checked, remove it from the list, do not process any adjacent squares.
                adjacents.remove([adj_x,adj_y])
            elif checked[adj_y][adj_x] == True:
                continue
            else:                                                           # If it is NOT a 9
                value, adj_spaces, adj_values = get_adjacents(adj_x,adj_y)  # get the adjacent spaces
                checked[adj_y][adj_x] = True                                # mark it as checked
                basin_size += 1                                             # increase the basin size
                adjacents.remove([adj_x,adj_y])                             # remove it from the list
                for space in (space for space in adj_spaces if space not in new_adjacents):   # for this space's adjacents not already staged
                    if checked[space[1]][space[0]] == True:  #If checked already, skip.
                        pass
                    elif datamap[space[1]][space[0]] == 9:   #If a 9, mark as checked, skip.
                        checked[space[1]][space[0]] = True
                        pass
                    else:                                                   
                        new_adjacents.append(space)          # Otherwise, add it to the list to check
            
    return basin_size

low_points, risk = get_low_points(datamap, height, width)
for point in low_points: 
     basin_sizes.append(get_basin_size(datamap,checked,point))

print("Part 1 Answer: ",risk)
print("Part 2 Answer:", sorted(basin_sizes)[-1] * sorted(basin_sizes)[-2] * sorted(basin_sizes)[-3])
