previous_line = 0
current_line = 0
count = 0
input = open("day1_input.txt", "r")
data = input.readlines()
for x in data:
    current_line = int(x)
    print(f"The current value is {current_line} and the previous value is {previous_line}.")
    if current_line > previous_line:
        count += 1
        print(f"The current value is greater than the prior value and the new count is {count}.")
    else:
        print(f"The current value is equal to or less than the prior value and the count remains {count}.")
    previous_line = current_line

#count - 1 to remove the fact that the first line is greater than nothing.
print(count - 1)
#1709 

next_window = []
previous_window = 0
count = 0

input = open("day1_input.txt", "r")
data = input.readlines()
for x in data:
    current_window = next_window
    next_window = []
    current_window.append(int(x))
    if len(current_window) < 3:
        print("still building window...")
        next_window = current_window
    elif len(current_window) == 3:
        if sum(current_window) > previous_window:
            print("greater")
            count +=1
        previous_window = sum(current_window)
        print(current_window)
        next_window.append(current_window[1])
        next_window.append(current_window[2])
        print(next_window)

#count - 1 to remove the fact that the first window is greater than nothing.
print(count - 1)
#1761
