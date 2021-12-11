board = [['-','-','-'],['-','-','-'],['-','-','-']]

def printBoard():
    print('Printing board...')
    for i in board:
        print(i)

def noError(row, col):
    if (row>2 or row<0) or (col>2 or col<0):
        print('**** Invalid row or column. Please select row / col between values 0 to 2 ****')
        print('**** Invalid choice. Please mark again! ****')
        return False
    if board[row][col] != '-':
        print('**** Board[' + str(row) + '][' + str(col) + '] has already been selected. Please select somewhere else on the board ****')
        print('**** Invalid choice. Please mark again! ****')
        return False
    return True 

def winBoard():
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != '-':
            return True
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != '-':
            return True 
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '-':
        return True
    if board [0][2] == board [1][1] and board[1][1] == board[2][0] and board[0][2] != '-':
        return True
    return False 

def tieBoard():
    count = 0
    for i in range(3):
        count += board[i].count('-')
    return count 

printBoard()

turn = 0
marker = ['X', 'O']
won = False

while not won:
    print('Player ' + str(turn%2+1) + ', make your move')
    row = int(input('Enter row nos (0-2):'))
    col = int(input('Enter col nos (0-2):'))
    if noError(row, col):
        print('Player ' + str(turn%2+1) + ' added mark at the location ' + str(row) + ',' + str(col))
        board[row][col] = marker[(turn%2)]
        printBoard()
        if winBoard():
            print('Player ' + str(turn%2+1) + ' wins! Game Over!')
            won = True 
            continue
        if tieBoard() == 0:
            print('Game is tied. No winner.')
            won = True
            continue
        turn += 1
    else:
        continue 
