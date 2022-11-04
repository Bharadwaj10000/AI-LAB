import random 
finalBoard = ["-"]*10
#player moves (pm)
pm = [] 
#computer moves (cm)
cm = [] 
winPattern = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]] 
def showBoard(): 
    k = 1
    for i in range(1,10): 
        print(finalBoard[i],end=" ") 
        if(i%3==0): 
         print() 
 
def playerTurn(symbol): 
    pos = int(input()) 
    while(pos not in pm and pos not in cm): 
        print("Enter a valid position : (1-9) ") 
        finalBoard[pos] = symbol
        pm.append(pos) 
#cs -> computer symbol
#ps -> player symbol
def computerTurn(cs,ps): 
    for i in range(1,10): 
        board = finalBoard[:] 
        if i not in cm and i not in pm: 
         makeMove(board, cs, i) 
         if isWinner(board,cs): 
          return i 
    for i in range(1,10): 
        board = finalBoard[:] 
        if i not in pm and i not in cm: 
            makeMove(board, ps, i) 
            if(isWinner(board,ps)): 
                return i 
    move = chooseRandomMoveFromList([1,3,7,9]) 
    if move != None: 
        return move 
    if finalBoard[5]=="-":
         return 5
    return chooseRandomMoveFromList([2,4,6,8]) 

def isWinner(board,symbol): 
    for pattern in winPattern: 
     if(board[pattern[0]]==symbol and board[pattern[1]]==symbol and board[pattern[2]]==symbol): 
        return True
    return False
def isTie(cs,ps): 
    if isWinner(finalBoard,ps)==False and isWinner(finalBoard,cs)==False : 
        return True
    return False
def makeMove(board,letter,pos): 
    board[pos] = letter 
 
def chooseRandomMoveFromList(movesList): 
    possibleMoves = [] 
    for i in movesList: 
        if i not in pm and i not in cm: 
            possibleMoves.append(i) 
    if(len(possibleMoves)!=0): 
        return random.choice(possibleMoves) 
    else: 
        return None
 
def start(): 
    #computer starts the game everytime 
    plays = 0
    flag = False
    print("Enter Your Symbol : ") 
    playerSymbol = input() 
    if(playerSymbol == "X" or playerSymbol == "x"): 
        computerSymbol = "O"
        playerSymbol = "X"
    else: 
        playerSymbol = "O"
        computerSymbol = "X"
    print("\nYour symbol is : ",playerSymbol) 
    #flag represents whether the game is over or not 
    while(plays <= 8 and flag != True): 
        if(flag != True): 
            print("Player Turn : \n") 
            print("Enter your position (1-9) ") 
            playerTurn(playerSymbol) 
            showBoard() 
            flag = isWinner(finalBoard, playerSymbol) 
        
        if(flag != True): 
            print("Computer Turn : \n") 
            pos = computerTurn(computerSymbol,playerSymbol) 
            cm.append(pos) 
            finalBoard[pos] = computerSymbol 
            showBoard() 
            flag = isWinner(finalBoard,computerSymbol) 
        plays = plays + 2
    if(flag != True): 
        print("Computer Turn :\n") 
        computerTurn(computerSymbol,playerSymbol) 
        if(isWinner(finalBoard,computerSymbol)): 
            print("Computer Won the game ") 
        elif(isWinner(finalBoard,playerSymbol)): 
            print("You won the game ") 
        else: 
            print("TIE GAME") 
    print("Final Board : ") 
    showBoard() 
 
 
start() 


