winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
def display_board():
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
def player_input(mark):
    while True:
        inp = int(input(f"[player] '{mark}' Enter your choice:"))
        if int(inp) < 10 and int(inp) > 0:
            if board[inp] == " ":
                return inp
            else:
                print(f"[player] '{mark}' place already taken.")
        else:
            print(f"[player] '{mark}' Enter valid option (1 - 9).")
def winning(mark, board):
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == mark:
            return True
def win_move(i, board, mark):
    temp_board = list(board)
    temp_board[i] = mark
    if winning(mark, temp_board):
        return True
    else:
        return False
def AI_input(AI, player, board):
    for i in range(1, 10):
        if board[i] == ' ' and win_move(i, board, AI):
            return i
    for i in range(1, 10):
        if board[i] == ' ' and win_move(i, board, player):
            return i
    for i in [5, 1, 7, 3, 2, 9, 8, 6, 4]:
        if board[i] == ' ':
            return i
def win_check(player, AI):
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == AI:
            print('[AI] wins the match!')
            return False
    if ' ' not in board:
        print('MATCH DRAW!!')
        return False
    return True
def main_game():
    global board
    play = True
    board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player, AI = 'x', 'o'
    display_board()
    while play:
        if player == 'x':
            x = player_input(player)
            board[x] = player
            display_board()
            play = win_check(player, AI)
            if play:
                o = AI_input(AI, player, board)
                print(f'[AI] Entered:{o}')
                board[o] = AI
                display_board()
                play = win_check(player, AI)
        else:
            x = AI_input(AI, player, board)
            print(f'[AI] Entered:{x}')
            board[x] = AI
            display_board()
            play = win_check(player, AI)
            if play:
                o = player_input(player)
                board[o] = player
                display_board()
                play = win_check(player, AI)
main_game()