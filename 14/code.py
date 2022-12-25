import argparse
from time import time
import json
import math

DAY = 14

PUZZLE_TEXT = """
--- Day 14: Extended Polymerization ---

The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has polymerization equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer template and a list of pair insertion rules (your puzzle input). You just need to work out what polymer would result after repeating the pair insertion process a few times.

For example:

NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C

The first line is the polymer template - this is the starting point of the process.

The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.
Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

Your puzzle answer was 2988.

--- Part Two ---

The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

Your puzzle answer was 3572761917024.
"""

SAMPLE_INPUT = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

PUZZLE_INPUT = """
VFHKKOKKCPBONFHNPHPN

VS -> B
HK -> B
FO -> P
NC -> F
VN -> C
BS -> O
HS -> K
NS -> C
CV -> P
NV -> C
PH -> H
PB -> B
PK -> K
HF -> P
FV -> C
NN -> H
VO -> K
VP -> P
BC -> B
KK -> S
OK -> C
PN -> H
SB -> V
KO -> P
KH -> C
KS -> S
FP -> B
PV -> B
BO -> C
OS -> H
NB -> S
SP -> C
HN -> N
FN -> B
PO -> O
FS -> O
NH -> B
SO -> P
OB -> S
KC -> C
OO -> H
BB -> V
SC -> F
NP -> P
SH -> C
BH -> O
BP -> F
CC -> S
BN -> H
SS -> P
BF -> B
VK -> P
OV -> H
FC -> S
VB -> S
PF -> N
HH -> O
HC -> V
CH -> B
HP -> H
FF -> H
VF -> V
CS -> F
KP -> F
OP -> H
KF -> F
PP -> V
OC -> C
PS -> F
ON -> H
BK -> B
HV -> S
CO -> K
FH -> C
FB -> F
OF -> V
SN -> S
PC -> K
NF -> F
NK -> P
NO -> P
CP -> P
CK -> S
HB -> H
BV -> C
SF -> K
HO -> H
OH -> B
KV -> S
KN -> F
SK -> K
VH -> S
CN -> S
VC -> P
CB -> H
SV -> S
VV -> P
CF -> F
FK -> F
KB -> V
"""

P1_SAMPLE_SOLUTION = 1588

P2_SAMPLE_SOLUTION = 2188189693529


def elapsed_time(start_time):
    return f"{round(time() - start_time, 8)}s\n"


class Puzzle:
    def __init__(self, input_text):
        self.input_text = input_text
        self.input_list = input_text.strip().split("\n")
        self.template = self.input_list[0]
        self.instructions = {}

        for inst in [line.split(" -> ") for line in self.input_list if "->" in line]:
            self.instructions[inst[0]] = [inst[0][0] + inst[1], inst[1] + inst[0][1]]

    def start(self):
        self.letters = {}
        self.pairs = {}
        for i in range(0, len(self.template)):
            try:
                self.letters[self.template[i]] += 1
            except:
                self.letters[self.template[i]] = 1
            pair = self.template[i : i + 2]
            if len(pair) == 2:
                try:
                    self.pairs[pair] += 1
                except:
                    self.pairs[pair] = 1

        pass

    def step(self):
        step = {}
        for pair, count in self.pairs.items():
            pairs = self.instructions[pair]
            try:
                step[pair] -= count
            except:
                step[pair] = count * -1
            try:
                step[pairs[0]] += count
            except:
                step[pairs[0]] = count
            try:
                step[pairs[1]] += count
            except:
                step[pairs[1]] = count
            try:
                self.letters[pairs[0][1]] += count
            except:
                self.letters[pairs[0][1]] = count

        for pair, count in step.items():
            try:
                self.pairs[pair] += count
            except:
                self.pairs[pair] = count

    def p1(self):
        self.start()
        for i in range(0, 10):
            self.step()

        counts = []
        for letter, count in self.letters.items():
            counts.append(count)

        self.p1_solution = max(counts) - min(counts)

    def p2(self):
        self.start()
        for i in range(0, 40):
            self.step()

        counts = []
        for letter, count in self.letters.items():
            counts.append(count)

        self.p2_solution = max(counts) - min(counts)


def main():
    parser = argparse.ArgumentParser(description=f"AOC2022 Puzzle Day { DAY }")
    parser.add_argument(
        "-p", "--showpuzzle", help="Display Puzzle Text", action="store_true"
    )
    parser.add_argument(
        "-s", "--showsample", help="Display Sample Input", action="store_true"
    )
    args = parser.parse_args()

    if args.showpuzzle:
        print(f"###############\nAOC 2022 DAY {DAY} PUZZLE TEXT\n###############")
        print(PUZZLE_TEXT)

    if args.showsample:
        print(f"###############\nAOC 2022 DAY {DAY} SAMPLE INPUT\n###############")
        print(SAMPLE_INPUT.strip())
        print(
            f"\n###############\nAOC 2022 DAY {DAY} P1 SAMPLE SOLUTION\n###############"
        )
        print(P1_SAMPLE_SOLUTION)
        print(
            f"\n###############\nAOC 2022 DAY {DAY} P2 SAMPLE SOLUTION\n###############"
        )
        print(P2_SAMPLE_SOLUTION)

    if P1_SAMPLE_SOLUTION:
        print("PART 1\nTesting Sample...\n")
        start_time = time()
        sample = Puzzle(input_text=SAMPLE_INPUT)
        sample.p1()
        if P1_SAMPLE_SOLUTION == sample.p1_solution:
            print("Sample correct.")
        else:
            print(
                f"Sample failed; Expected {P1_SAMPLE_SOLUTION}, got {sample.p1_solution}"
            )
        print(f"Elapsed time {elapsed_time(start_time)}")
        if PUZZLE_INPUT:
            puzzle = Puzzle(input_text=PUZZLE_INPUT)
            puzzle.p1()
            print("Processing Input...\n")
            start_time = time()
            print(f"SOLUTION: {puzzle.p1_solution}")
            print(f"Elapsed time {elapsed_time(start_time)}")

    if P2_SAMPLE_SOLUTION:
        print("PART 2\nTesting Sample...\n")
        start_time = time()
        sample.p2()
        if P2_SAMPLE_SOLUTION == sample.p2_solution:
            print("Sample correct.")
        else:
            print(
                f"Sample failed; Expected {P2_SAMPLE_SOLUTION}, got {sample.p2_solution}"
            )
        print(f"Elapsed time {elapsed_time(start_time)}")
        if PUZZLE_INPUT:
            puzzle.p2()
            print("Processing Input...\n")
            start_time = time()
            print(f"SOLUTION: {puzzle.p2_solution}")
            print(f"Elapsed time {elapsed_time(start_time)}")


if __name__ == "__main__":
    main()
