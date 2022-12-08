#p1
fish = []
days = 80
input = open("day6_input.txt")

data = input.readline().strip().split(',')
for d in data:
    fish.append(int(d))

for day in range(0,days):
    for f in range(0,len(fish)):
        if fish[f] == 0:
            fish[f] = 6
            fish.append(8)
        else:
            fish[f] -= 1
    
print(len(fish))

# p2 first try that took hours because i tracked every fish individually

# doing it this way takes hours...
fish = []
days = 256
input = open("day6_input.txt")

data = input.readline().strip().split(',')
for d in data:
    fish.append(int(d))

for day in range(0,days):
    for f in range(0,len(fish)):
        if fish[f] == 0:
            fish[f] = 6
            fish.append(8)
        else:
            fish[f] -= 1
    
print(len(fish))

# p2 second try that did it the right way, kinda, but without the deque

# doing it this way takes a second lol. 

counter = [0,0,0,0,0,0,0,0,0]
holder = [0,0,0,0,0,0,0,0,0]
days = 256
input = open("day6_input.txt")


data = input.readline().strip().split(',')
for d in data:
    counter[int(d)] += 1

for _ in range(256):
    holder[8] = counter[0]              #everything that was at 0 spawns a new fish with a timer of 8
    holder[7] = counter[8]              #everything at 8 ticks to 7
    holder[6] = counter[0] + counter[7] #everything that was at 7 ticks to 6, everything that was at 0 resets to 6
    holder[5] = counter[6]              #everything that was at 6 ticks to 5
    holder[4] = counter[5]              #everything that was at 5 tucks to 4
    holder[3] = counter[4]              #everything that was at 4 ticks to 3
    holder[2] = counter[3]              #everything that was at 3 ticks to 2
    holder[1] = counter[2]              #everything that was at 2 ticks to 1
    holder[0] = counter[1]              #everything that was at 1 ticks to 0
    counter = holder                    #the new values take their place
    holder = [0,0,0,0,0,0,0,0,0]        #i don't understand why but unless i explicitly empty the holder, 
                                        #when it loops through, it adds counter[x] to holder[x-1] instead of just assigning?

print(sum(counter))


