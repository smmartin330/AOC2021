# part 1

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

# part 2

input = open("day3_input.txt", "r")
o2_data = input.readlines()
input.close()

for pos in range(0,12):
    print(f"position {pos}")
    count = 0
    ones = 0
    zeroes = 0
    for v in reversed(o2_data): #what is the most common value for the data in this position
        count += 1 #how many records?
        if v[pos] == "1":
           ones += 1 #if i find a one, add 1
        if v[pos] == "0":
           zeroes += 1 #if i find a zero, add 1
    
    print(f"{ones} ones and {zeroes} zeroes out of {count} values.")
    count = 0
    for v in reversed(o2_data): #now go through the data and keep or discard data
        count += 1
        if len(o2_data) > 1:
            if ones >= zeroes and int(v[pos]) == 1:
                #one is most common OR they are equal, positional value is one, we keep
                pass
            elif zeroes > ones and int(v[pos]) == 0 :
                #zero is most common, positional value is zero, we keep.
                pass
            else: 
                #we remove the value.
                pass
                o2_data.remove(v)

input = open("day3_input.txt", "r")
co2_data = input.readlines()
input.close()

for pos in range(0,12):
    print(f"position {pos}")
    count = 0
    ones = 0
    zeroes = 0
    for v in reversed(co2_data): #what is the most common value for the data in this position
        count += 1 #how many records?
        if v[pos] == "1":
           ones += 1 #if i find a one, add 1
        if v[pos] == "0":
           zeroes += 1 #if i find a zero, add 1
    
    print(f"{ones} ones and {zeroes} zeroes out of {count} values.")
    count = 0
    for v in reversed(co2_data): #now go through the data and keep or discard data
        count += 1
        if len(co2_data) > 1:
            if ones > zeroes and int(v[pos]) == 0:
                #zero is least common, value is zero, keep.
                pass
            elif zeroes > ones and int(v[pos]) == 1 :
                #zero is most common, positional value is one, we keep.
                pass
            elif zeroes == ones and int(v[pos]) == 0:
                pass
            else: 
                #we remove the value.
                pass
                co2_data.remove(v)

print(int(o2_data[0][0:12],2) * int(co2_data[0][0:12],2))
        
