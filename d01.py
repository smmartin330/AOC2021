previous_line = 0
current_line = 0
count = 0
input = open("d01_input.txt", "r")
data = input.readlines()
for x in data:
    current_line = int(x)
    if current_line > previous_line:
        count += 1
    previous_line = current_line

#count - 1 to remove the fact that the first line is greater than nothing.
print(count - 1)
#1709 

next_window = []
previous_window = 0
count = 0

input = open("d01_input.txt", "r")
data = input.readlines()
for x in data:
    current_window = next_window
    next_window = []
    current_window.append(int(x))
    if len(current_window) < 3:
        next_window = current_window
    elif len(current_window) == 3:
        if sum(current_window) > previous_window:
            count +=1
        previous_window = sum(current_window)
        next_window.append(current_window[1])
        next_window.append(current_window[2])

#count - 1 to remove the fact that the first window is greater than nothing.
print(count - 1)
#1761
