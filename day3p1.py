x_accum = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma = ""
epsilon = ""
input = open("day3_input.txt", "r")
data = input.readlines()
for x in data:
    for position in range(0,12):
        x_accum[position] += int(x[position])

for position in range(0,12):
    if x_accum[position] >= 500:
        gamma = gamma+"1"
        epsilon = epsilon+"0"
    else:
        gamma = gamma+"0"
        epsilon = epsilon+"1"

print(int(gamma, 2) * int(epsilon,2))
