# def read_file(path):
#     """reads the contents of the textfile"""
#     with open(path, "r") as boards:
#         bingo_input = boards.read()
#         bingo_input = repr(bingo_input)
#         return bingo_input


# def call_numbers(bingo_input):
#     """extract numbers called"""
#     return bingo_input.split("\\n\\n")[0][1:]


# def get_boards(bingo_input):
#     """extract bingo boards"""
#     # get rid of final speech mark
#     bingo_boards = bingo_input[:-1]
#     # split into boards
#     bingo_boards = bingo_boards.split("\\n\\n")[1:]
#     # split by row
#     board_rows = [board.split("\\n") for board in bingo_boards]
#     # tidy up rows
#     boards = []
#     for board in board_rows:
#         rows = []
#         for row in board:
#             row = row.split()
#             rows.append(list(map(int, row)))
#         boards.append(rows)
#     return boards


# global game_finished
# game_finished = False


# def call_out_numbers(bingo_calls, boards):
#     """format callouts and then for each callout calls the next function/s"""
#     bingo_calls = list(map(int, bingo_calls.split(",")))
#     for call in bingo_calls:
#         cross_out_call(boards, call)


# def cross_out_call(boards, call):
#     """checks each call against the bingo boards and 'crosses them out' then checks for bingo"""
#     for board in boards:
#         for row in board:
#             if call in row:
#                 # replace number from call with an "x"
#                 position = row.index(call)
#                 row.pop(position)
#                 row.insert(position, "x")
#         check_for_bingo(board, call)


# def check_for_bingo(bingo_board, last_call):
#     """checks if whole row/column is "x"/bingo and then calls function to calculate score"""
#     global game_finished
#     columns = []
#     column = []
#     # construct columns
#     for j in range(5):
#         for i in range(5):
#             column.append(bingo_board[i][j])
#         columns.append(column)
#         column = []
#         if game_finished == False:
#             for row in bingo_board:
#                 if row.count("x") == 5:
#                     print(evaluate_score(bingo_board, last_call))
#             for col in columns:
#                 if col.count("x") == 5:
#                     print(evaluate_score(bingo_board, last_call))


# def evaluate_score(bingo_board, last_call):
#     """evaluates final score by multiplying the last call with all non crossed out numbers"""
#     global game_finished
#     game_finished = True
#     count = 0
#     for row in bingo_board:
#         for num in row:
#             if num != "x":
#                 count += num
#     return count * last_call


# path = "bingo_part1.txt"
# bingo_input = read_file(path)
# bingo_calls = call_numbers(bingo_input)
# boards = get_boards(bingo_input)
# call_out = call_out_numbers(bingo_calls, boards)


def read_file(path):
    """reads the contents of the textfile"""
    with open(path, "r") as boards:
        bingo_input = boards.read()
        bingo_input = repr(bingo_input)
        return bingo_input


def call_numbers(bingo_input):
    """extract numbers called"""
    return bingo_input.split("\\n\\n")[0][1:]


def get_boards(bingo_input):
    """extract bingo boards"""
    # get rid of final speech mark
    bingo_boards = bingo_input[:-1]
    # split into boards
    bingo_boards = bingo_boards.split("\\n\\n")[1:]
    # split by row
    board_rows = [board.split("\\n") for board in bingo_boards]
    # tidy up rows
    boards = []
    for board in board_rows:
        rows = []
        for row in board:
            row = row.split()
            rows.append(list(map(int, row)))
        boards.append(rows)
    return boards


def call_out_numbers(bingo_calls, boards):
    """format callouts and then for each callout calls the next function/s"""
    bingo_calls = list(map(int, bingo_calls.split(",")))
    for call in bingo_calls:
        cross_out_call(boards, call)


def cross_out_call(boards, call):
    """checks each call against the bingo boards and 'crosses them out' then checks for bingo"""
    for board in boards:
        for row in board:
            if call in row:
                # replace number from call with an "x"
                position = row.index(call)
                row.pop(position)
                row.insert(position, "x")
        check_for_bingo(board, call)


def check_for_bingo(bingo_board, last_call):
    """checks if whole row/column is "x"/bingo and then calls function to calculate score"""
    columns = []
    column = []
    # construct columns
    for j in range(5):
        for i in range(5):
            column.append(bingo_board[i][j])
        columns.append(column)
        column = []
    for row in bingo_board:
        if row.count("x") == 5:
            print(evaluate_score(bingo_board, last_call))
    for col in columns:
        if col.count("x") == 5:
            print(evaluate_score(bingo_board, last_call))


def evaluate_score(bingo_board, last_call):
    """evaluates final score by multiplying the last call with all non crossed out numbers"""
    count = 0
    for row in bingo_board:
        for num in row:
            if num != "x":
                count += num
    return count * last_call


path = "bingo_part1.txt"
bingo_input = read_file(path)
bingo_calls = call_numbers(bingo_input)
boards = get_boards(bingo_input)
call_out = call_out_numbers(bingo_calls, boards)
