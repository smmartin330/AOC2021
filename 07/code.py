import argparse
from time import time
from statistics import mean,median
from math import floor

DAY = 0

PUZZLE_TEXT = '''
--- Day 7: The Treachery of Whales ---

A giant whale has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!

Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you! They seem to be preparing to blast a hole in the ocean floor; sensors indicate a massive underground cave system just beyond where they're aiming!

The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your submarine to get through. However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?

There's one major catch - crab submarines can only move horizontally.

You quickly make a list of the horizontal position of each crab (your puzzle input). Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.

For example, consider the following horizontal positions:

16,1,2,0,4,2,7,1,2,14
This means there's a crab with horizontal position 16, a crab with horizontal position 1, and so on.

Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position 2:

Move from 16 to 2: 14 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 0 to 2: 2 fuel
Move from 4 to 2: 2 fuel
Move from 2 to 2: 0 fuel
Move from 7 to 2: 5 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 14 to 2: 12 fuel
This costs a total of 37 fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).

Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?

Your puzzle answer was 352331.

--- Part Two ---

The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?

As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes 5:

Move from 16 to 5: 66 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 0 to 5: 15 fuel
Move from 4 to 5: 1 fuel
Move from 2 to 5: 6 fuel
Move from 7 to 5: 3 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 14 to 5: 45 fuel
This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 fuel instead.

Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?

Your puzzle answer was 99266250.
'''

SAMPLE_INPUT = '''
16,1,2,0,4,2,7,1,2,14
'''

PUZZLE_INPUT = '''
1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65,20,4,0,1001,65,1,65,1106,0,8,99,35,67,101,99,105,32,110,39,101,115,116,32,112,97,115,32,117,110,101,32,105,110,116,99,111,100,101,32,112,114,111,103,114,97,109,10,68,48,111,357,88,6,709,901,43,700,591,1146,317,930,727,806,194,1053,1093,819,530,2,1545,281,257,869,7,161,104,272,847,281,258,322,1076,214,1783,1499,55,985,220,1429,524,734,99,1067,1547,255,99,987,668,1095,529,233,324,61,23,45,259,169,13,618,1286,1293,468,1677,457,147,139,34,310,267,1132,451,529,853,324,779,0,554,91,72,694,442,79,1243,118,56,15,869,1075,931,33,585,392,15,15,861,1163,632,857,157,155,468,1073,299,1261,44,0,123,448,856,876,15,1032,310,322,1457,996,352,686,159,486,62,1035,540,685,242,198,1266,86,152,709,990,112,1479,605,274,233,1490,198,1349,2,1,666,628,878,262,960,709,414,740,322,389,45,517,1078,1030,884,286,300,101,671,286,948,209,354,1342,86,746,1308,181,479,300,129,45,5,1003,1006,584,309,16,1064,756,35,349,634,680,601,397,179,754,302,172,397,665,33,508,27,858,369,1236,19,228,854,206,32,17,1062,123,3,1140,80,240,60,497,937,83,249,91,550,317,72,808,1406,122,455,214,110,16,690,27,988,611,946,70,138,1730,1216,1073,20,439,806,222,965,517,1413,251,1,62,23,308,215,218,366,1025,142,450,50,76,682,698,1309,1286,318,460,554,23,268,543,780,425,1078,250,203,817,44,978,94,425,52,272,157,485,187,221,1,475,221,233,1183,1985,29,211,409,793,60,178,241,167,150,382,957,49,202,181,285,116,889,490,826,553,216,176,151,1710,536,1196,297,1112,715,258,387,392,950,1284,733,405,77,1310,74,287,6,321,117,286,127,380,680,197,143,416,110,1236,236,74,59,1100,64,10,30,135,12,1077,481,774,878,879,387,1502,327,17,88,486,238,168,201,1307,831,750,132,281,198,707,609,80,94,204,399,106,257,419,464,73,384,1944,112,669,45,497,334,95,1689,477,257,781,1007,417,626,361,440,474,719,13,42,184,1618,415,832,911,1237,169,481,43,977,59,734,346,367,146,642,298,390,1669,1319,724,1586,980,499,276,387,75,1042,14,58,653,532,1327,631,908,498,48,1576,1476,84,1457,1601,569,851,4,410,215,417,269,797,556,99,1703,520,1523,79,862,1086,578,686,394,1120,304,20,463,14,135,0,560,517,1164,132,791,304,725,1143,1246,111,57,513,247,243,269,209,181,98,294,68,18,106,75,190,153,193,219,16,467,955,767,1002,127,196,272,30,800,899,241,40,265,468,524,45,831,379,759,722,734,27,99,1383,80,351,686,44,77,136,386,95,901,135,334,1117,982,151,310,253,529,479,349,252,333,360,166,440,492,652,60,1591,219,456,1308,164,1117,93,670,477,558,76,154,67,111,321,356,899,1039,8,577,80,124,231,4,798,559,178,598,42,379,12,306,245,133,60,564,530,173,114,774,405,961,131,620,549,51,1437,9,22,553,301,987,245,1538,127,213,0,778,15,211,921,0,133,1166,280,240,1225,580,967,431,625,1162,213,120,186,1633,583,1542,102,3,97,516,123,676,564,774,12,34,938,1529,493,772,124,1441,287,679,231,1147,159,141,22,678,678,292,933,12,123,751,1656,1396,240,115,221,880,962,1237,1402,179,572,766,224,838,766,269,792,1727,166,30,315,293,757,201,934,1687,346,1962,8,627,228,16,440,33,414,212,1032,730,575,284,445,1356,141,707,779,920,407,858,326,232,356,444,302,165,42,460,1726,481,276,293,873,528,260,1060,197,154,682,180,154,1162,93,160,387,478,406,1138,987,435,727,148,582,163,210,766,632,257,732,276,205,32,489,456,70,1295,755,98,547,1295,334,1436,52,1292,185,1044,311,1122,630,588,560,54,1651,387,112,992,512,195,1333,1623,492,125,61,739,373,135,1436,280,580,7,291,71,875,112,680,852,89,455,309,129,173,530,90,245,921,1629,1592,465,146,1008,304,553,823,378,519,10,151,952,152,284,44,718,1,260,1268,94,1425,156,55,389,505,1176,487,596,16,888,26,1710,1232,1388,21,902,608,18,163,5,908,184,452,1362,493,261,595,1115,156,0,205,337,913,205,59,1143,99,538,1471,662,405,61,7,714,575,216,470,341,149,759,1286,414,367,79,134,426,41,389,1191,188,17,1227,27,929,798,21,81,65,1381,593,1360,106,760,505,1125,364,370,18,89,826,33,256,941,687,38,715,1091,175,1451,1,263,311,927,1893,681,565,364,113,1205,849,129,98,384,495,1785,804,60,128,852,93,983
'''

P1_SAMPLE_SOLUTION = 37

P2_SAMPLE_SOLUTION = 168

def elapsed_time(start_time):
    return f"{round(time() - start_time, 8)}s\n"

class Puzzle():
    def __init__(self,input_text):
        self.input_text = input_text
        self.input_list = input_text.strip().split(',')
        self.crabs = [ int(crab) for crab in self.input_list ]
    
    def tri(self, n):
        return n * (n + 1) // 2
    
    def p1(self):
        self.p1_solution = int(sum([abs(crab - median(self.crabs)) for crab in self.crabs]))

    def p2(self):
        self.p2_solution = min([sum([self.tri(abs(crab - floor(mean(self.crabs)))) for crab in self.crabs]),sum([self.tri(abs(crab - round(mean(self.crabs)))) for crab in self.crabs])])

def main():
    parser = argparse.ArgumentParser(description=f'AOC2022 Puzzle Day { DAY }')
    parser.add_argument("-p", "--showpuzzle", help="Display Puzzle Text", action='store_true')
    parser.add_argument("-s", "--showsample", help="Display Sample Input", action='store_true')
    args = parser.parse_args()
    
    if args.showpuzzle:
        print(f"###############\nAOC 2022 DAY {DAY} PUZZLE TEXT\n###############")
        print(PUZZLE_TEXT)
    
    if args.showsample:
        print(f"###############\nAOC 2022 DAY {DAY} SAMPLE INPUT\n###############")
        print(SAMPLE_INPUT.strip())
        print(f"\n###############\nAOC 2022 DAY {DAY} P1 SAMPLE SOLUTION\n###############")
        print(P1_SAMPLE_SOLUTION)
        print(f"\n###############\nAOC 2022 DAY {DAY} P2 SAMPLE SOLUTION\n###############")
        print(P2_SAMPLE_SOLUTION)
    

    if P1_SAMPLE_SOLUTION:            
        print("PART 1\nTesting Sample...\n")
        start_time = time()
        sample = Puzzle(input_text=SAMPLE_INPUT)
        sample.p1()
        if P1_SAMPLE_SOLUTION == sample.p1_solution:
            print("Sample correct.")
        else:
            print(f"Sample failed; Expected {P1_SAMPLE_SOLUTION}, got {sample.p1_solution}")
        print(f"Elapsed time {elapsed_time(start_time)}")
        if PUZZLE_INPUT:
            puzzle = Puzzle(input_text=PUZZLE_INPUT)
            puzzle.p1()
            print("Processing Input...\n")
            start_time = time()
            print(f'SOLUTION: {puzzle.p1_solution}')
            print(f"Elapsed time {elapsed_time(start_time)}")
        
    if P2_SAMPLE_SOLUTION:
        print("PART 2\nTesting Sample...\n")
        start_time = time()
        sample.p2()
        if P2_SAMPLE_SOLUTION == sample.p2_solution:
            print("Sample correct.")
        else:
            print(f"Sample failed; Expected {P2_SAMPLE_SOLUTION}, got {sample.p2_solution}")
        print(f"Elapsed time {elapsed_time(start_time)}")
        if PUZZLE_INPUT:
            puzzle.p2()
            print("Processing Input...\n")
            start_time = time()
            print(f'SOLUTION: {puzzle.p2_solution}')
            print(f"Elapsed time {elapsed_time(start_time)}")
    
if __name__ == "__main__":
    main()