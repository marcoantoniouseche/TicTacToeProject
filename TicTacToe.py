#In this part, i make the board and display it
board = [['[ ]','[ ]','[ ]'], ['[ ]','[ ]','[ ]'], ['[ ]','[ ]','[ ]']]

for i in range(len(board)):
    print(i + 1, board[i][0], board[i][1], board[i][2])
print('  ', 1,' ',2,' ',3)

#add interactivity 
print('Select "O" if you want to play with o, or "X" if you want to play with x')
letter_select = input()
letter_select = letter_select.capitalize()

print('Instructions:\nFor fill it the squares, write vertical and horizontal numbers depend of the position on board\ne.g.'
' if you write 12 you should output:')
print(f'''
1 [ ] [{letter_select}] [ ]
2 [ ] [ ] [ ]
3 [ ] [ ] [ ]
   1   2   3
''')
print('Warning: If you type an incorrect value, you will lost your turn\n')

counter = 0
i1 = 0 #Refers to index one
i2 = 0 #Refers to index two
victory = False #Boolean value that i use to look at if you winner or not

while counter < 9:
    i1 = 0
    try: 
        player1 = int(input('player1: '))
        while player1 >= 10:
            player1 -= 10
            i1 += 1
        i2 = player1
        if board[i1-1][i2-1] == '[O]' or board[i1-1][i2-1] == '[X]':
            print('Invalid value, lost your turn')
            counter -= 1
        else:
            board[i1-1][i2-1] = '[O]'
    except IndexError:
        print('Invalid value, lost your turn')
        counter -= 1
    for i in range(len(board)):
        print(i + 1, board[i][0], board[i][1], board[i][2])
    print('  ', 1,' ',2,' ',3)
    counter += 1
    
    if counter == 9:
        break
    
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] == '[O]' or board[i][0] == board[i][1] == board[i][2] == '[X]':
            victory = True
        if board[0][i] == board[1][i] == board[2][i] == '[O]' or board[0][i] == board[1][i] == board[2][i] == '[X]':
            victory = True
        
    if victory == True:
        break
    
    if board[2][0] == board[1][1] == board[0][2] == '[O]' or board[0][0] == board[1][1] == board[2][2] == '[O]' or board[2][0] == board[1][1] == board[0][2] == '[X]' or board[0][0] == board[1][1] == board[2][2] == '[X]':
        break
    
    i1 = 0
    try:
        player2 = int(input('player2: '))
        while player2 >= 10:
            player2 -= 10
            i1 += 1
        i2 = player2
        if board[i1-1][i2-1] == '[O]' or board[i1-1][i2-1] == '[X]':
            print('Invalid value, lost your turn')
            counter -= 1
        else:
            board[i1-1][i2-1] = '[X]'
    except IndexError:
        print('Invalid value, lost your turn')
        counter -= 1
    for i in range(len(board)):
        print(i + 1, board[i][0], board[i][1], board[i][2])
    print('  ', 1,' ',2,' ',3)
    counter += 1
    
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] == '[O]' or board[i][0] == board[i][1] == board[i][2] == '[X]':
            victory = True
        if board[0][i] == board[1][i] == board[2][i] == '[O]' or board[0][i] == board[1][i] == board[2][i] == '[X]':
            victory = True
        
    if victory == True:
        break
    
    if board[2][0] == board[1][1] == board[0][2] == '[O]' or board[0][0] == board[1][1] == board[2][2] == '[O]' or board[2][0] == board[1][1] == board[0][2] == '[X]' or board[0][0] == board[1][1] == board[2][2] == '[X]':
        break