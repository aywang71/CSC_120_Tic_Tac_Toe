board = [['-','-','-'],['-','-','-'],['-','-','-']]

def printBoard():
    print('Printing board...')
    for i in board:
        print(i)

def errorCheck(row, col):
    if (row>2 or row<0) or (col>2 or col<0):
        print('**** Invalid row or column. Please select row / col between values 0 to 2 ****')
        print('**** Invalid choice. Please mark again! ****')
        return False
    if board[row][col] != '-':
        print('**** Board[' + str(row) + '][' + str(col) + '] has already been selected. Please select somewhere else on the board ****')
        print('**** Invalid choice. Please mark again! ****')
        return False
    return True 


printBoard()

turn = 0
marker = ['X', 'O']

while turn <= 3:
    print('Player ' + str(turn%2+1) + ', make your move')
    row = int(input('Enter row nos (0-2):'))
    col = int(input('Enter col nos (0-2):'))
    if errorCheck(row, col):
        print('Player ' + str(turn%2+1) + ' added mark at the location ' + str(row) + ',' + str(col))
        board[row][col] = marker[(turn%2)]
        printBoard()
        turn += 1
    else:
        continue 
