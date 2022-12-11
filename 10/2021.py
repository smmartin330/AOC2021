import d10data

### DAY 10: SYNTAX SCORING
### PROCESS THE NAVIGATION SUBSYSTEM OUTPUT FOR SYNTAX ERRORS. STOP AT FIRST ERROR ON EACH LINE. 
### CALCULATE THE SCORE FOR THE FIRST ILLEGAL CHARACTER IN A LINE.
### INITIAL THOUGHT: TRACK HOW MANY OF EACH BRACKET AS BEEN OPENED, REDUCE THE COUNT WHEN CLOSED.
### IF IT GOES NEGATIVE, THAT'S AN ERROR. 
### INITIAL THOUGHT WAS WAY OVERTHINKING IT. IF TRYING TO CLOSE A PAIR NOT JUST OPENED, BAD.

chunks = {  "(": 0,
            "[": 0,
            "{": 0,
            "<": 0,
            "last": ""
            }


p1_scores = {   ")": 3,
                "]": 57,
                "}": 1197,
                ">": 25137
}

p2_scores = {   "(": 1,
                "[": 2,
                "{": 3,
                "<": 4
}

pair = {    ")": "(",
            "]": "[",
            "}": "{",
            ">": "<",
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">"
            }

def process_line(line):
    opened = []
    for char in list(line):
        if char in "({[<":
            opened.append(char)
        if char in ")}]>":
            if opened[-1] != pair[char]:
                #print(F"Syntax Error! Expected {pair[opened[-1]]} but got {char}")
                return p1_scores[char],opened
            else: 
                opened.pop()    

    return 0,opened

def part_one(data):
    total_score = 0

    for d in data.split('\n'):
        total_score += process_line(d)[0]

    return total_score

def part_two(data):
    line_scores = []

    for d in data.split('\n'):
        
        if process_line(d)[0] == 0:
            line_score = 0
            opened = list(reversed(process_line(d)[1]))
            for c in opened:
                line_score = (line_score * 5) + p2_scores[c]

            line_scores.append(line_score)

    return list(sorted(line_scores))[len(line_scores)//2]


p1_sample = part_one(d10data.sample)
p1_my = part_one(d10data.my)
p2_sample = part_two(d10data.sample)
p2_my = part_two(d10data.my)

print(f"Part 1 Sample Answer: {p1_sample} | My Answer {p1_my}")
print(f"Part 2 Sample Answer: {p2_sample} | My Answer {p2_my}")
