#In this part, i make the board and display it
board = [['[ ]','[ ]','[ ]'], ['[ ]','[ ]','[ ]'], ['[ ]','[ ]','[ ]']]

for i in range(len(board)):
    print(i + 1, board[i][0], board[i][1], board[i][2])
print('  ', 1,' ',2,' ',3)