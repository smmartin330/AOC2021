signal = []
output = []
patterns = []
line_count = 0
output_total = 0

file = open("day8_input.txt")

contents = file.readlines()

#read in the data
for line in contents:
    remap = {   "0": [],
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": [],
                "6": [],
                "7": [],
                "8": [],
                "9": [],
            }
    
    rewire = {  "a": "",
                "b": "",
                "c": "",
                "d": "",
                "e": "",
                "f": "",
                "g": "",
    }
    
    patterns = []

    signal.append(line.split('|')[0].strip())
    output.append(line.split('|')[1].strip())

    # We know that if it has all 2, 3, 4, or 7 segments, it is a 1, 7, 4, or 8 respectively.

    for x in signal[line_count].split():
        if sorted(x) not in patterns:
            if len(x) == 7:
                #print(f"8 is {sorted(x)}")
                remap["8"] = sorted(x)
            elif len(x) == 3:
                #print(f"7 is {sorted(x)}")
                remap["7"] = sorted(x)
            elif len(x) == 4:
                #print(f"4 is {sorted(x)}")
                remap["4"] = sorted(x)
            elif len(x) == 2:
                #print(f"1 is {sorted(x)}")
                remap["1"] = sorted(x)
            else:
                patterns.append(sorted(x))

    # We know that the SEGMENT THAT IS IN A 7 BUT NOT IN A 1 is the "a" segment.

    for segment in remap["7"]:
        if segment not in remap["1"]:
            rewire["a"] = segment
            #print(f"a is {segment}")

    # We know that OUT OF THE THREE DIGITS WITH 6 SEGMENTS, THE ONE THAT HAS the A and the values from the 4 is the 9. 5 OF 10 DIGITS IDENTIFIED.
    for pattern in patterns:
        if len(pattern) == 6 and all(x in pattern for x in remap["4"]):
            remap["9"] = pattern
            patterns.remove(pattern)
    
    # The remaining two 6 segment digits, the one that DOES NOT HAVE THE VALUES FROM THE 1 is the 6, and the other is the 0. 7 of 10 digits identified.    
    for pattern in patterns:
        if len(pattern) == 6 and all(x in pattern for x in remap["1"]):
                remap["0"] = pattern
                patterns.remove(pattern)

    for pattern in patterns:
        if len(pattern) == 6:
            remap["6"] = pattern
            patterns.remove(pattern)

    #The value that is IN THE 9 but NOT IN THE 6 or 1 is C. the other value from the 1 is therefore F. We now know 0, 1, 4, 6, 7, 8, 9 and A, C, and F.
    for x in remap["9"]:
        if x in remap["1"] and x not in remap["6"]:
            rewire["c"] = x
            for f in remap["1"]:
                if x != f:
                    rewire["f"] = f
   
    # THE FIVE SEGMENT VALUE that contains the SEGMENTS FROM THE 7 is the 3. we now know 0, 1, 2, 3, 4, 6, 7, 8, 9. 
    for pattern in patterns:
        if len(pattern) == 5 and all(x in pattern for x in remap["7"]):
            remap["3"] = pattern
            patterns.remove(pattern)

    # The FIVE SEGMENT PATTERN that is NOT in the 9 is the 2. We now know the 2, and the segment from the 2 not in the 9 is E. 
    for pattern in patterns:
        if len(pattern) == 5 and not all(x in remap["9"] for x in pattern):
            remap["2"] = pattern
            patterns.remove(pattern)
            for x in pattern:
                if x not in remap["9"]:
                    rewire["e"] = x

    # THE REMAINING PATTERN is the 5. 
    remap["5"] = patterns[0]
    
    #once values are known, parse the data.
    row_value = ""
    for d in output[line_count].split():
        digit = sorted(d)
        match_found = False
        for k,v in remap.items():
            if sorted(v) == sorted(digit) and match_found == False:
                row_value = row_value+k
                match_found = True
        if match_found == False:
            row_value = row_value+"?"
    try:
        output_total += int(row_value)
    except:
        print("Decryption failed.")
        quit()

    line_count += 1

print(output_total)
