import argparse
from time import time

DAY = 13

PUZZLE_TEXT = """
--- Day 13: Transparent Origami ---

You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:

6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper and . is an empty, unmarked position:

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:

#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....
Because this is a vertical line, fold left:

#####
#...#
#...#
#...#
#####
.....
.....
The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

How many dots are visible after completing just the first fold instruction on your transparent paper?

Your puzzle answer was 621.

--- Part Two ---

Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?

Your puzzle answer was HKUJGAJZ.


"""

SAMPLE_INPUT = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

PUZZLE_INPUT = """
323,511
1240,588
1210,140
641,365
23,232
26,448
206,791
1208,779
1141,210
209,796
1012,63
1032,700
473,327
925,120
612,669
1148,711
333,323
405,509
577,735
315,635
1002,50
1158,403
388,885
746,796
709,672
929,868
224,191
679,883
939,581
442,453
380,511
136,670
455,173
1253,423
1019,546
1094,764
224,555
293,834
611,278
636,844
89,799
1052,147
1205,603
823,287
335,767
358,438
700,275
1116,214
919,252
485,61
462,724
303,435
1223,621
487,738
73,227
1057,431
667,859
965,831
1094,549
211,143
1141,497
67,129
631,11
961,294
448,57
25,298
641,280
216,764
1304,318
636,443
569,679
979,679
792,709
398,739
562,709
517,746
1143,290
1032,271
698,469
718,585
584,739
495,287
441,803
1071,561
208,777
972,232
249,385
629,74
584,36
704,719
922,837
321,96
85,290
169,210
897,215
626,836
806,103
1047,642
915,317
976,542
912,709
246,65
1210,84
987,127
741,231
723,478
991,844
467,605
584,410
282,565
338,36
922,703
470,380
956,446
418,322
1205,267
33,614
1097,315
605,539
1284,325
1064,450
446,434
144,306
1205,627
987,663
1133,590
185,341
851,691
1148,376
70,603
345,271
1141,397
965,63
890,812
761,625
1066,513
882,311
381,868
485,833
674,50
323,663
975,319
517,148
1148,885
1066,157
632,432
758,115
1043,677
756,532
1064,849
720,833
726,812
1118,52
733,47
823,604
1001,271
216,101
323,767
55,184
838,86
72,413
840,380
97,508
1026,642
922,750
465,233
1284,121
592,289
847,334
612,791
751,640
766,885
64,385
1215,338
298,662
315,707
256,67
1261,91
162,457
319,767
187,717
930,383
705,803
726,306
995,635
400,705
487,511
797,341
561,187
102,779
262,61
354,513
549,603
244,210
935,844
328,70
249,735
1228,466
1228,684
1058,206
430,32
1017,168
584,82
107,161
938,329
510,418
300,261
1136,267
793,633
843,289
1255,184
1064,45
748,754
152,170
155,144
162,631
1173,347
995,707
43,616
1044,891
991,687
947,348
1246,61
726,261
910,705
126,329
6,318
249,159
952,232
63,467
769,579
1021,318
1037,65
1133,529
390,869
118,434
1174,224
1287,232
1051,868
544,120
259,868
869,385
952,456
88,464
26,224
405,681
621,614
120,700
1307,112
1089,792
326,771
60,505
729,667
1240,603
1223,190
269,11
574,177
321,273
594,527
213,173
142,738
224,787
605,91
914,147
157,658
700,658
843,737
283,278
1171,717
497,449
1064,444
1054,603
976,576
815,607
514,635
902,333
564,796
741,646
395,865
1126,604
309,63
900,605
17,327
718,533
441,579
636,2
1200,99
82,71
418,572
326,323
843,583
1066,737
237,351
231,340
377,691
23,11
1161,451
1212,509
592,586
1017,840
872,735
465,457
1061,385
1143,831
518,709
1284,224
862,649
290,721
1037,0
1205,827
89,302
792,485
244,381
1243,129
385,229
547,597
381,0
146,5
1221,799
726,709
167,596
555,203
1039,485
425,610
353,148
1054,155
838,808
1266,51
64,509
562,185
423,554
1006,875
469,553
823,511
259,864
463,334
636,892
1073,351
580,654
994,26
63,875
1197,763
559,340
938,453
309,607
1200,795
57,459
905,159
574,333
800,588
515,311
70,288
98,49
20,151
1089,102
299,143
659,679
70,36
1303,239
441,315
167,604
162,337
1178,886
629,771
1089,550
382,513
939,726
637,607
960,875
221,67
1155,144
584,709
44,51
994,232
823,578
1205,515
375,844
509,287
935,396
659,112
591,19
800,418
818,263
1174,9
1021,576
528,565
139,759
206,21
1133,81
700,843
1164,5
1011,639
1203,597
395,129
12,775
385,568
1033,691
167,511
793,746
654,45
850,680
497,584
442,567
206,873
100,362
89,95
934,819
763,597
157,768
984,518
766,680
949,60
279,113
515,456
711,857
448,425
733,159
273,829
224,32
890,730
350,168
388,639
87,190
679,11
13,753
85,696
1148,631
1235,453
387,665
749,707
1230,450
119,318
795,456
472,808
1061,681
216,325
142,879
391,252
291,348
442,439
758,144
661,173
1091,851
97,386
764,728
648,318
146,665
186,849
592,533
80,717
744,16
385,120
1240,306
587,317
249,509
343,844
1293,327
454,565
862,57
1041,883
549,515
256,709
253,675
390,810
216,549
323,127
1099,751
284,642
843,311
467,737
1098,439
167,298
992,357
211,751
1246,509
572,823
741,663
782,329
345,63
266,389
922,639
129,648
354,261
321,845
1057,675
1086,704
299,255
216,774
388,437
917,494
393,400
1051,864
177,590
785,246
1031,333
1153,658
396,147
964,50
1005,742
372,441
959,148
626,120
149,443
385,774
723,577
726,155
584,588
1230,444
1041,326
266,505
572,876
792,185
328,571
157,61
44,684
606,194
1300,186
922,144
1017,616
610,843
137,522
733,735
139,347
954,383
1168,156
627,222
1310,401
813,124
358,232
1153,320
1031,844
565,592
118,882
266,57
105,603
651,148
674,2
102,115
856,331
718,309
584,633
518,185
1223,854
249,61
746,98
751,332
1044,639
44,843
741,696
1205,647
863,502
577,159
684,836
1019,348
141,341
304,875
87,264
1223,829
95,780
361,60
43,278
651,215
1295,498
971,187
358,662
110,383
863,766
1166,451
269,217
758,526
933,579
1303,368
13,141
555,691
1173,323
649,273
398,155
830,627
544,885
105,647
631,680
157,124
146,889
1066,210
594,437
246,45
610,171
1143,604
63,19
574,513
689,738
1007,435
877,739
1225,679
699,840
991,50
677,70
186,45
1143,596
315,259
682,261
48,754
945,576
1071,406
846,381
11,35
7,368
162,885
995,259
293,278
110,9
490,109
1223,704
738,876
206,343
813,320
1006,14
1148,337
410,18
256,185
174,179
689,614
162,845
438,735
559,338
1048,61
1148,437
689,156
1071,488
63,427
567,704
518,829
885,610
572,684
406,10
552,368
745,592
281,22
350,14
249,213
1061,159
365,318
234,185
27,222
309,803
309,271
425,732
1066,375
213,315
1079,340
887,554
627,672
1250,255
1084,583
107,597
507,844
85,198
293,840
933,691
392,833
584,185
447,766
184,290
261,848
723,420
244,829
887,562
592,605
577,47
1148,681
1273,770
989,798
1181,694
763,161
98,845
1031,561
185,329
909,463
1001,495
410,605
704,175
1049,400
266,891
956,633
299,367
162,290
796,635
927,485
1017,60
1257,446
735,10
321,798
1027,278
965,679
298,63
77,847
736,513
1266,684
920,25
700,171
229,284
698,103
1006,616
388,837
1284,849
309,175
413,215
459,691
908,654
674,443
304,19
909,431
1284,401
455,582
278,194
1287,11
1266,236
572,338
1250,389
726,633
1215,332
320,800
1292,50
833,813
1307,351
1171,347
231,858
142,156
137,323
72,861
87,829
900,338

fold along x=655
fold along y=447
fold along x=327
fold along y=223
fold along x=163
fold along y=111
fold along x=81
fold along y=55
fold along x=40
fold along y=27
fold along y=13
fold along y=6
"""

P1_SAMPLE_SOLUTION = 17

P2_SAMPLE_SOLUTION = None


def elapsed_time(start_time):
    return f"{round(time() - start_time, 8)}s\n"


class Puzzle:
    def __init__(self, input_text):
        self.input_text = input_text
        self.input_list = input_text.strip().split("\n")
        self.dots = [dot.split(",") for dot in self.input_list if "," in dot]
        self.dots = [[int(dot[0]), int(dot[1])] for dot in self.dots]
        self.folds = [fold.split("=") for fold in self.input_list if "fold" in fold]

    def fold(self, fold):
        f, p = fold[0][-1], int(fold[1])

        match f:
            case "x":
                new_dots = [dot for dot in self.dots if dot[0] < p]
                # folding along the x axis, so x's to the right of the fold move left
                # if the fold fold is x 3 the dot's x positon is (5,2)
                # f = 3, x = 5, it should end up at 1. new x = f - (x - f)
                for dot in [dot for dot in self.dots if dot[0] > p]:
                    x = p - (dot[0] - p)
                    y = dot[1]
                    new_dot = [x, y]
                    if new_dot not in new_dots:
                        new_dots.append([x, y])

            case "y":
                new_dots = [dot for dot in self.dots if dot[1] < p]
                # folding along the x axis, so x's to the right of the fold move left
                # if the fold fold is x 3 the dot's x positon is (5,2)
                # f = 3, x = 5, it should end up at 1. new x = f - (x - f)
                for dot in [dot for dot in self.dots if dot[1] > p]:
                    x = dot[0]
                    y = p - (dot[1] - p)
                    new_dot = [x, y]
                    if new_dot not in new_dots:
                        new_dots.append([x, y])

        self.dots = new_dots

    def p1(self):
        self.fold(self.folds[0])
        self.p1_solution = len(self.dots)

    def p2(self):
        for fold in self.folds:
            self.fold(fold)
        height = max([dot[1] for dot in self.dots]) + 1
        width = max([dot[0] for dot in self.dots]) + 1
        display = []
        for row in range(0, height):
            display.append([" "] * width)
        for dot in self.dots:
            display[dot[1]][dot[0]] = "O"
        self.p2_solution = "\n"
        for row in display:
            for char in row:
                self.p2_solution += char
            self.p2_solution += "\n"


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
