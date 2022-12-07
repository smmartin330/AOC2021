import argparse
from time import time
import numpy
import math

DAY = 0

PUZZLE_TEXT = '''
--- Day 4: Giant Squid ---

You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

Your puzzle answer was 21607.

--- Part Two ---

On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?

Your puzzle answer was 19012.
'''

SAMPLE_INPUT = '''
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''

PUZZLE_INPUT = '''
72,99,88,8,59,61,96,92,2,70,1,32,18,10,95,33,20,31,66,43,26,24,91,44,11,15,48,90,27,29,14,68,3,50,69,74,54,4,16,55,64,12,73,80,58,83,6,87,30,41,25,39,93,60,9,81,63,75,46,19,78,51,21,28,94,7,17,42,53,13,97,98,34,76,89,23,86,52,79,85,67,84,47,22,37,65,71,49,82,40,77,36,62,0,56,45,57,38,35,5

91 60 70 64 83
35 41 79 55 31
 7 58 25  3 47
 2 23 69 59 21
11 22  8 87 90

77 95 19 21 76
93 92 62 35  3
 4 29  7 41 45
80 50 83 61 64
39 32 91 56 48

47 11 39 58 97
63 51 40 74 71
12 17 68 81 44
64 85 20 84 80
 0 77  5 18 50

44 82 32  1 57
98 88 33 83 85
25 61 63 99 37
 0 74  7 20 39
71 72 22 80 28

78 97  0 48 41
56 51 62 58 90
 8 44 98 46  1
38 40 91 20 55
88  2 32 86 14

84 50 16 45 40
 9 39 60 34 46
57 20 12  3 36
58 17 72 48 83
73 85 49 67 66

 4 30 73 83 57
74 23 49 19 42
72 65  8 99 13
25  6 82 53 68
20 86 46 48 50

52 29 61 16 75
36 19  2 82  9
34 90 89 43 14
69 66 20 21 11
31 53 46 18 23

37 76 34 79 99
43  5 42 91 71
47 54 19 82 81
95 78 65 60 24
32 94 92 27 66

68 61 80 90 53
33 17 52  0 23
30 71  5 85 11
27 39 41  6  9
58 98  7 74 89

31  5 55 67 51
54 86 40 25 92
91 62  9 94  7
39  0 44 52 28
12 17 26 46 32

94 80 83 88 77
65 71 31 86  0
98 55 18 92 72
 6 12 30 25 34
67 53 14 20 47

81 74 14 47  1
83 82  4 89  8
43 93 63 21 44
92 61 25 77 97
12 72 35 78 52

26 39 13 37 46
87  6 58 47 19
24 35 45 95 52
 5 27 42 96  0
23 64  8 29 83

53 58 18 96 93
57 90 35 88 68
91 89  7 80 47
59 86 81 24 31
43  8 66 17 94

 0 97 91 67 90
93 20 36  4 42
43 64 28 94 34
31  2  7 54 71
18 35 76 86 16

55 63 26 47  0
 2 23 54 25 90
36 13 85 31 15
59 51 18 88 62
44 69  9 81 58

26 97 98 42 27
 3 53 91 89 93
87 57 12 18  5
29 99 86 47 64
 6 28 92 79 67

 4 35 45 79 16
33 95 99 80  9
60 78 57 51 50
27  5 48 21 46
19 70 32 58 18

94 82 61 66 31
14 56 76 37 28
42 81 50 10 40
 2 98 47 29 62
69 90 46 44 18

87  3  8 50 17
15 90 54 45 21
 6 28 43 51 32
97 84 69 30 38
98 44 88 55 83

34 19 27 43 92
81 62 52 32 39
50 29 83 25 82
60 55 49 41 97
75 94 22 69 66

59 39 96 87 65
33 18  4 71 15
22 27 92  8 29
19  5 32 85 45
91 79 35  9  3

41 53 51 68 85
72 71 94 82 81
60 38 13 16  7
49 80 10  0 54
20 39 59 64 99

37 21 90 40 73
85 75 16 34 99
84 15 25 18 27
77 32  0 76 36
13 50 68 91 12

24 26  0 14 12
89  4 15 95 73
54  2 55 84 42
30 50 81 60 87
37 94 71 91 53

52  1 81 44 34
27 60 36 19 69
98 11 49 67 56
77 72 40 48 66
84  9 37 32 51

58 15  7 36 55
94 49 69 89 87
79 70 30 77 19
68 31 56 41 53
47 85 74 54 46

64 87 23 66  0
29 98 72 82 80
70 45 46 30 37
53 54 33 86 76
 6 75 71 68  2

12 31 43 80 41
37 15 13  2  3
86 61  9 17 59
55 68 72  8  1
96 26 44 73 47

67 39 95 84 10
 5 88 13 81 99
68 15 98  6 17
47 85 74 32 97
58  8 16 56 42

82 31 42 84 17
25 28  2  6 12
78 57 16 97 18
87 64 54 30 65
 3 77 29 49 81

24  1 43 89 46
29 78 57 14 85
 9 58 53 83 35
96 42 62 68 74
67  2 39 37 51

72 26 46 52  3
91 27 41 32 53
25 36  7 63 22
56 38 93 65  9
95 19 77 64 44

21 71 13 99 39
47 17 80 85 64
 5 18 48 27 81
82 23 45 57 12
83 55 26 31 32

57 13 86 69 65
42 76 35 18 39
17 91 95 43  6
55 97 22 54 14
56  0  5 60 92

87 12 46 42 35
44  6 95 30 67
51 21 68 37 59
77 65 50 69 63
33 56 24 57 28

82 87 42 99 39
38 55 74 28  6
77 66  9 80 10
47 90 32  3 98
92 52  5 94 51

16  1 87 57 66
41 70 58 31  5
71 88 17 42 76
81 40 25 89 63
92  4 61 77 64

70 28 56 51 66
44 60 25  0 45
91 78 81 95 88
75 43 57 67 32
58 27 20 82 22

16 98 82 79 90
96  4 80 69 19
 9 28 33 40 94
 2 99 14 73 43
76 68 74 42 30

29 42 94 45  2
25 81 46 54 26
75 99 51 58 23
76 72 71 64 63
66 70 92 44 13

 2 71 39 49 95
19 84  1  7 96
 9  6 60 93 78
38 91 55 36 41
64  3 10 20 74

79 80 15 69 89
36 76 83  7 72
87 34 48  0 93
 5 84 77 20 75
46 27 11 55  3

82 34  4 14 74
40 39  7  6 95
11 51 78 80 29
97 81 38  9 71
22 62 19 72 68

54 70 90 43 98
12 27 57 96 62
32 76  0 86 42
88 68 81 91 50
10 94 18 71  2

90 41 29 53 58
59 62 14 85 66
25 82 68 44 93
73 32 76 67 18
94 71 83 34 37

 6 72 69 33 90
87 60 66 85 16
59 80 86 47 89
32 98 17 29  5
48 27 18 57 81

10 22 98 86 82
 8 66 71 14 93
87 79 40 78 49
84 63 17 54 94
35 39 47  1 96

58 60 52  6 86
41 20 66 59  2
92 79 88 40 71
96  9 25 36 17
91 32 43 38  8

74  3 64 66 68
69 37 22 76 33
17 67 29 32 27
63 49 46 21 60
35 73  9 52 50

 0 91  8 26  9
 3 98 79 97  7
37 61  1 60 47
86 17 11 70 15
66 53  2 90 54

68 42  0 78 16
83 88 21 87 12
50  2 29 14 63
72 90 81 71 91
54 79 94 10  4

28 63 97 31  4
50 52 43 24 16
36 77  0  9 75
83 94 69 68 27
93 82 42 56 34

24 52 66 51 82
50 30 34 93 67
56 70 53 13 78
 4 84 88 57 81
80 74  5 95 98

56 64 53 52 72
51 48 50 60 49
 8 46 84 95 43
91 21  7 88 33
94 57 80 25 54

70 57 62 20 18
86 45 41 76 32
87 35 52  5  2
16 77 25 39 22
38 10  6 29 98

89 54 57 80 65
 0 38 94 15  6
85 76 16 83 59
92  5 53 14 95
47 35 73 98 34

64 24 90 71 69
55 35 20 98 41
94 70 10 73 16
65 84 60  7 72
83  2 22 78 99

31 81 74 56 98
13 97 95 49 67
 9 47 42 99 60
38 22 65 58 21
82 45  2 28 68

90 88 28 85 51
23 93 13 55 50
63 22  3 30 39
 5 71 82 95 81
57 76 12 92 56

78 12 28  6 73
59 24 43 29 31
30 34 75 52 48
62 57 23 74 50
91 92  5 95 38

95 88 13 22 10
16  4 19 37 91
50 52 60 46 77
45 55 49 41 26
21  7 67 48 18

51 79 44 16 71
 6 13 12 41 97
50 25 19 63  4
98  0 23 77 31
27 57 52 99  3

86 95  7 54 84
50 33 48 16  9
82 32 38  6 34
43 80 27 37 11
89 70 41 22 45

24  3 47 68 35
85 76  8 29  4
 2 10  5 28 73
92 89 50 25 56
99 57 79 19 37

 0 46 72  5 20
62 28 24 53 44
84 25 63 34  9
75  1 65 59 10
95 29 97 77 45

87 90  1 17 67
57 73 35 10 30
65 14 46 60  6
70 66 56 69 92
 3 27 21 64 88

20 58 53 29 66
27  6 67 89 33
88 60 79 69 97
90  3 47 68 25
48 59 42 98 39

65 90 45 97 87
75 98  7 58 42
51  4 95 88 47
94  6 11 53 63
49 80  2 48 68

 3 77 42 97 82
70 58 81 18 47
78 96 62 39 56
22 87 71 31 94
34 48 57 38 88

70 36 65 33 45
71  0 59 44  1
42 37  7  5  9
11 12 91 43 27
60 21 57 61 99

76 75 56 49  2
36 57 39 64 77
95 19 35 43 97
82 34 50 44 55
45 74 15 66 29

 0 75  1 78 79
13 37 48 27 14
90 50 26 92 67
89 62 87 69 33
29 47  4  2 12

74 42 24 86 61
92 66  3 65 75
 7  1 77 63 64
39 91 87 28  5
30 35 41 73 96

 0 81 41 15 66
62 19 86 31 40
23 94 98 82 24
61 99  1  5 60
80 64 91 33 47

16 61 56 77 57
28 59 71 45 92
53 20 35 66 73
99  3 86 31 74
94 69 84 96 90

71 56 23 76 42
90 44 58 27 15
46 18 86 63 24
69 49 82 38 43
33 51 60 66 39

75 78 38 25 76
67  3 83 90 10
40 89 47 23 88
34 21 46 16 33
 9 79 50  0 26

81 75 80 23 41
62  4 76  1 63
56 39 57 28 61
20  6 79 92 84
88  3 90 16 12

87 78  3 34 63
98 21 24  9 99
62 29 57 65 27
47 52 67 76 71
11 17 93 23 82

53 68 70 38 56
62 54 25 43 35
 9  3 13 15 75
59 27 26 33 83
93 40 11 64 76

27 83 26 48 77
51 20 65 18 35
80 30 60 44 89
84 82 62 91 63
12 97 11 19 34

31 28 92 48 34
 9 93 61 71 60
52 18 97 81 62
80 64 57 22 30
11 88 74 29 56

57 34 90 46 73
31  0 70 66 82
45 12 40 19 87
91 24 59 83 14
80 21 13 86 89

 9  8 64 48 30
 6 62 28 99 41
79 45 83  7 55
15 14 54 88 12
90 74 97 96 50

50 73 58 26 12
96 98 56 34  7
51 92 14 89 16
41 70 80 55 13
37 47  2 64 99

98  9 70 17 18
39 15 88 16 47
80 41  8 51 21
54 42 31 10 59
37 92 33 62 68

60 72 51 63 29
83 39 41 24 14
34  5 94 90 56
75 80 67 17 20
47 11 58 93 42

97  7 27 42 67
12 30 91 45 52
62 50 87 92 71
99 84 33  6 46
29 55 86 47 60

25 49 55 98 22
66  9 61 59 90
45 74 77 88  5
 6 76  0 36 93
23 70 33 95  2

53 92 27 86 55
66 52 26 58 38
 2 78 69 62 65
30  5  1 25 99
76 43  4 13  8

18 72 51 48 39
62 19 28 44 82
54 22 38 55 83
86 93 42  9 32
11 89 27 34 68

85 99 35 88 76
10 25 33 83 70
54 81 77 73 66
 4 74 96 41 86
49  3 68 65 39

71  0 70 14 31
28 23 17 43 75
13 40 38 87 97
63 93 92 89 27
58 76 24 53 54

55 58 11 38 16
98 86 13 12  8
22 10 77 61 90
37 76  2 62 45
44 30 52 70 82

89 55 12 90 63
40 88 91 22 74
 8  0 25  6 79
53 23 87 77 20
11 38 78 43 94

21 14 37  8 16
29 73 67 91 56
 5 90 12 92 59
64  1 42 72 94
98 86 18 69 49

79 71 82  1 77
96 39 24 60 81
49 16 12 63 14
 0 32 78 37  8
92 33 15 99 65

54 11 40 55 33
58 47  4 83 94
46 96 16 28  5
 0 62 95 71 39
93 59  7 75 64
'''

P1_SAMPLE_SOLUTION = 4512

P2_SAMPLE_SOLUTION = 1924

class Puzzle():
    def __init__(self,input_text):
        self.input_text = input_text
        self.input_list = input_text.strip().split('\n')
        self.draws = self.input_list[0].split(',')
    
    def initialize_boards(self):
        self.boards = []
        board = []
        for line in [ line for line in self.input_list if len(line) == 14 ]:
            board.append(line.split())
            if len(board) == 5:
                self.boards.append(Board(board))
                board = []
        
    def p1(self):
        self.initialize_boards()
        for draw in self.draws:
            for board in self.boards:
                check_board = board.draw_number(draw)
                if check_board:
                    self.p1_solution = check_board
                    return True

    def p2(self):
        self.initialize_boards()
        for draw in self.draws:
            winner = []
            for board in self.boards:
                check_board = board.draw_number(draw)
                if check_board:
                    winner.append(board)
                    if len(self.boards) == 1:
                        self.p2_solution = check_board
                        return True
            if len(winner) > 0:
                for board in winner:
                    self.boards.remove(board)
            
class Board():
    def __init__(self,board):
        self.rows = board
        self.columns = numpy.transpose(self.rows).tolist()
        self.all_spaces = []
        [ self.all_spaces.extend(x) for x in self.rows]
        self.all_spaces = [ eval(x) for x in self.all_spaces ]
        self.all_draws = []
        
    def draw_number(self,draw):
        self.all_draws.append(draw)
        if int(draw) in self.all_spaces:
            self.all_spaces.remove(int(draw))
        
        for row in self.rows:
            if all(x in self.all_draws for x in row):
                return sum(self.all_spaces) * int(draw)
        
        for col in self.columns:
            if all(x in self.all_draws for x in col):
                return sum(self.all_spaces) * int(draw)
        
        return False

def elapsed_time(start_time):
    return f"{round(time() - start_time, 8)}s\n"
        
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
        print("PART 1\nRunning Sample...\n")
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
            print("Running Input...\n")
            start_time = time()
            print(f'SOLUTION: {puzzle.p1_solution}')
            print(f"Elapsed time {elapsed_time(start_time)}")
        
    if P2_SAMPLE_SOLUTION:
        print("PART 2\nRunning Sample...\n")
        start_time = time()
        sample.p2()
        if P2_SAMPLE_SOLUTION == sample.p2_solution:
            print("Sample correct.")
        else:
            print(f"Sample failed; Expected {P2_SAMPLE_SOLUTION}, got {sample.p2_solution}")
        print(f"Elapsed time {elapsed_time(start_time)}")
        if PUZZLE_INPUT:
            print("Running Input...\n")
            puzzle.p2()
            start_time = time()
            print(f'SOLUTION: {puzzle.p2_solution}')
            print(f"Elapsed time {elapsed_time(start_time)}")
    
if __name__ == "__main__":
    main()