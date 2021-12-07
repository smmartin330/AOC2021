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
