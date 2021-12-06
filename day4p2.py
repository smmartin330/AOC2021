calls = []
boards = []
start_boards = {}
game_boards = {}
board_count = 0
input = open("day4_input.txt")

line = input.readline()

while line != "":

    split_line = line.split()

    if len(split_line) == 1:
        calls = split_line[0].split(',')

    elif line == "\n":
        pass

    else:

        board_count += 1

        boards.append(board_count)
        game_boards[board_count] = { "B" : [0,0,0,0,0], 
                                     "I" : [0,0,0,0,0],
                                     "N" : [0,0,0,0,0], 
                                     "G" : [0,0,0,0,0], 
                                     "O" : [0,0,0,0,0]  }
        start_boards[board_count] = { "B" : [], 
                                     "I" : [],
                                     "N" : [], 
                                     "G" : [], 
                                     "O" : []  }
        
        while len(split_line) == 5:
            start_boards[board_count]["B"].append(split_line[0])
            start_boards[board_count]["I"].append(split_line[1])
            start_boards[board_count]["N"].append(split_line[2])
            start_boards[board_count]["G"].append(split_line[3])
            start_boards[board_count]["O"].append(split_line[4])

            line = input.readline()
            split_line = line.split()
            
    line = input.readline()

input.close()

for call in calls:
    if len(boards) == 0:
        break
    for board in range(1,board_count+1):        
        if board in boards:
            for column in "BINGO":
                for spot in range(0,5):
                    if start_boards[board][column][spot] == call:
                        game_boards[board][column][spot] = 1
                        if game_boards[board][column] == [1,1,1,1,1]:
                            boards.remove(board)
                            last_call = call
                            last_board = board
                            break
                        elif game_boards[board]["B"][spot] == 1 and game_boards[board]["I"][spot] == 1 and game_boards[board]["N"][spot] == 1 and game_boards[board]["G"][spot] == 1 and game_boards[board]["O"][spot] == 1:
                            try:
                                boards.remove(board)
                                last_board = board
                            except:
                                pass
                            break
                        else:
                            pass
    last_call = call

total = 0

for column in "BINGO":
    for spot in range(0,5):
        if game_boards[last_board][column][spot] != 1:
            total += int(start_boards[last_board][column][spot])

print(int(last_call) * total)
