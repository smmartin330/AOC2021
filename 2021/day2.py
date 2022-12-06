#part1

x = 0
y = 0

input = open("day2_input.txt", "r")
data = input.readlines()
for d in data:
    #print(f"the command is {d}")
    command = d.split()
    #print(f"it was split into {command}")
    if command[0] == "forward":
        #print(f"x was {x}")
        x = x +  int(command[1])
        #print(f"new x is {x}")
    elif command[0] == "backward":
        #print(f"x was {x}")
        x = x -  int(command[1])
        #print(f"new x is {x}")
    elif command[0] == "down":
        #print(f"y was {y}")
        y = y + int(command[1])
        #print(f"new y is {y}")
    elif command[0] == "up":
        #print(f"y was {y}")
        y = y - int(command[1])
        #print(f"new y is {y}")

#print(x)
#print(y)
print(x*y)

#part2

x = 0
y = 0
aim = 0
input = open("day2_input.txt", "r")
data = input.readlines()
for d in data:
    command = d.split()
    if command[0] == "forward":
        print(command)
        print(f"old x {x}")
        x = x +  int(command[1])
        print(f"new x {x}")
        print(f"old y {y}")
        y = y + (int(command[1])*aim)
        print(f"new y {y}")
        
    elif command[0] == "down":
        print(f"old aim {aim}")
        aim = aim + int(command[1])
        print(f"new aim {aim}")

    elif command[0] == "up":
        print(f"old aim {aim}")
        aim = aim - int(command[1])
        print(f"new aim {aim}")


#print(x)
#print(y)
print(x*y)
