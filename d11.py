import d11data

### DAY X: DUMBO OCTOPUSES
### TRACKING THE ENERGY LEVEL OF OCTOPUSES.
### 
flashed = []
grid = []

sample_flashes = 0
my_flashes = 0
def make_grid(data):
    grid = []
    for line in data.split('\n'):
        grid.append([int(char) for char in line])
    
    return grid

def step(grid,x):
    all_true = [[True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True]]
    flashed = []
    flashes = 0
    for row in range(0,10):
        grid[row] = list(map(lambda x : x + 1, grid[row]))
        flashed.append([False, False, False, False, False, False, False, False, False, False])

    for row in range(0,10):
        for octopus in range(0,10):
            if grid[row][octopus] > 9 and flashed[row][octopus] != True:
                flash(row,octopus,flashed,grid)
    
    if flashed == all_true:
        print(x+1)

    for row in range(0,10):
        for octopus in range(0,10):
            if flashed[row][octopus] == True:
                grid[row][octopus] = 0
                flashes += 1
    
    return flashes

def flash(row,octopus,flashed,grid=grid):
    flashed[row][octopus] = True
    if row - 1 >= 0: # out of bounds protection
        if octopus - 1 >= 0: # out of bounds protection
            grid[row-1][octopus-1] += 1 # UP/LEFT                
        grid[row-1][octopus] += 1 # UP
        if octopus + 1 <= 9: # out of bounds protection
            grid[row-1][octopus+1] += 1 # UP/RIGHT
    
    if octopus - 1 >= 0: # out of bounds protection
        grid[row][octopus-1] += 1 #left
    
    if octopus + 1 <= 9: # out of bounds protection
        grid[row][octopus+1] += 1 #right
    
    if row + 1 <= 9: # out of bounds protection
        if octopus - 1 >= 0: # out of bounds protection
            grid[row+1][octopus-1] += 1 # DOWN/LEFT
        grid[row+1][octopus] += 1 # DOWN
        if octopus + 1 <= 9: # out of bounds protection
            grid[row+1][octopus+1] += 1 # DOWN/RIGHT
    
    for r in range(row-1,row+2):
        for o in range(octopus-1,octopus+2):
            if r in range(0,10) and o in range(0,10):
                if grid[r][o] > 9 and flashed[r][o] == False:
                    flash(r,o,flashed,grid)

    return

def main():
    sample_flashes = 0
    my_flashes = 0    
    
    sample_grid = make_grid(d11data.sample)
    my_grid = make_grid(d11data.my)
    
    for x in range(0,1000):
        sample_flashes += step(sample_grid,x)
        my_flashes += step(my_grid,x)
    
    print(sample_flashes)
    print(my_flashes)

if __name__ == '__main__':
    main()


#print(f"Part 1 Sample Answer: {p1_sample} | My Answer {p1_my}")
#print(f"Part 2 Sample Answer: {p2_sample} | My Answer {p2_my}")
