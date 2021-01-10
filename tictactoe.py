board = [' ' for x in range(10)]

def insertLetter(letter, pos) :
    board[pos] = letter

def spaceIsFree(pos) :
    return board[pos] == ' '

def printBoard(board) :
    print('   |   |')
    print(' ' + board[1] + ' | ' +board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' +board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' +board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(board, letter) :
    return (board[7] == letter and board[8] == letter and board[9] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[1] == letter and board[2] == letter and board[3] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[6] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter)

def playerMove() :
    run = True
    while run:
        move = input('Please select a position to place on \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('It\'s occupied')
            else: 
                print('Please make sure it is in the range')
        except:
            print('It must be a number!')


def compMove() :
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move
    
    edgesOpen = []
    for i in possibleMoves:
        if i in[2, 4, 6, 8]:
            edgesOpen.append(i)
    
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    
    return move


def selectRandom(li) :
    import random
    length = len(li)
    r = random.randrange(0, length)
    return li[r]

def isBoardFull(board) :
    if board.count(' ') > 1:
        return False
    else:
        return True

def main() :
    print("Let's play TicTacToe")
    printBoard(board)

    while not(isBoardFull(board)): 
        if not(isWinner(board, 'O')) :
            playerMove()
            printBoard(board)
        else :
            print("O\'s won!")
            break
        if not(isWinner(board, 'X')) :
            move = compMove()
            if move == 0 or isBoardFull(board):
                print("It is a draw!")
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in positon', move, ':')
                printBoard(board)
        else :
            print("X\'s won!")
            break

    # if isBoardFull(board) :
    #     print("It's a draw!")

main()