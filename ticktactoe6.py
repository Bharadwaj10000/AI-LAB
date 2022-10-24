def display_board():
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
def player_input(mark):
    while True:
        inp = input(f"[player] '{mark}' Enter your choice:")
        if inp.isdigit() and int(inp) <10 and int(inp) >0:
            inp = int(inp)
            if board[inp] == " ":
                return inp
            else:
                print(f"[player] '{mark}' place already taken.")
        else:
            print(f"[player] '{mark}' Enter valid option (1 - 9).")
def winning(mark,board):
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == mark:
            return True
def win_move(i,board,mark):
    temp_board = list(board)
    temp_board[i] = mark
    if winning(mark,temp_board):
        return True
    else:
        return False
def AI_input(AI , player , board):
    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,AI):
            return i
    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,player):
            return i
    for i in [5,1,7,3,2,9,8,6,4]:
        if board[i] == ' ':
            return i
def new_game():
    while True:
        chance = input('[player] Do you want to play again?(y/n):')
        if chance in['y','Y']:
            plays = True
            break
        elif chance in ['n','N']:
            print('Have a great day')
            plays = False
            break
        else:
            print('Enter correct input')
    if plays:
        print('play again')
        main_game()
    else:
        return False
def win_check(player , AI):
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == player:
            print('[player] wins the match!')
            if not new_game():
                return False
        elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == AI:
                print('[AI] wins the match!')
                if not new_game():
                    return False
    if ' ' not in board:
        print('MATCH DRAW!!')
        if not new_game():
            return False
    return True
def user_choice():
    while True:
        inp = input('[player]Choose your mark[x/o]: ')
        if inp in ['x' , 'X']:
            print('[player]You choose "X".\n[player]You play first.')
            return 'x','o'
        elif inp in ['O','o']:
            print('[player] You choose "O".\n[player] AI plays first.')
            return 'o','x'
        else:
            print('[player] Enter correct input!')
def main_game():
    global board
    play = True
    board =['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player , AI = user_choice()
    display_board()
    while play:
        if player == 'x':
            x = player_input(player)
            board[x] = player
            display_board()
            play = win_check(player , AI)
            if play:
                o = AI_input(AI , player , board)
                print(f'[AI] Entered:{o}')
                board[o] = AI
                display_board()
                play = win_check(player , AI)
        else:
            x = AI_input(AI , player , board)
            print(f'[AI] Entered:{x}')
            board[x] = AI
            display_board()
            play = win_check(player , AI)
            if play:
                o = player_input(player)
                board[o] = player
                display_board()
                play = win_check(player , AI)
main_game()