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
