#add Welcome message
print('\t\t\t\t-----Bienvenido a tic tac toe-----')
#this function verify if the value is integer or not
def catch(number):
    try:
        final_value = int(number)
    except ValueError:
        try:
            final_value = int(input('\tTipée un valor correcto(Entero):\n\t'))
        except ValueError:
            final_value = catch(number)
    return final_value

#this function verify if this value is 'O' or 'X'
def xoro(letter):
    while not(letter == 'X' or letter == 'x' or letter == 'O' or letter == 'o'):
        letter = input('\tTipée un valor correcto(\'X\' o \'O\'):\n\t')
    return letter

#This function display a board
def display_board(lis):
    for i in range(len(lis)):
        print('\t', i + 1, lis[i][0], lis[i][1], lis[i][2])
    print('\t','  ', 1,' ',2,' ',3)
    print('\n')
    
#this function assign 'X' or 'Y', depend of the player1 selection
def selection(player, favourite_figure):
    if player == 'Player1':
        if favourite_figure == 'X':
            return '[X]'
        else:
            return '[O]'
    else:
        if favourite_figure == 'X':
            return '[O]'
        else:
            return '[X]'

#In this part, i make the board and display it
board = [['[ ]','[ ]','[ ]'], ['[ ]','[ ]','[ ]'], ['[ ]','[ ]','[ ]']]

#add interactivity 
print('\n\tSeleccione "O" si quiere jugar con "O", o "X" si quiere jugar con "X"')
letter_select = xoro(input('\t'))
letter_select = letter_select.capitalize()

print('\n\tInstrucciones:\n\tPara llenar los cuadros, Escribe dos número, los cuales por separado representan la posición en el tablero de \n\tmanera horizontal vertical\n\te.g.'
' si escribes 12 tu deberías ver:')
print(f'''
\t1 [ ] [{letter_select}] [ ]
\t2 [ ] [ ] [ ]
\t3 [ ] [ ] [ ]
\t   1   2   3
''')
print('\tAdvertencia: Si tipea un valor incorrecto, pierdes el turno\n')

counter = 0
i1 = 0 #Refers to index one
i2 = 0 #Refers to index two
victory = False #Boolean value that i use to look at if you winner or not

while counter < 9:
    i1 = 0
    try: 
        player1 = catch(input('\tJugador1: '))
        while player1 >= 10:
            player1 -= 10
            i1 += 1
        i2 = player1
        if board[i1-1][i2-1] == '[O]' or board[i1-1][i2-1] == '[X]':
            print('\tValor inválido, pierdes el turno')
            counter -= 1
        else:
            board[i1-1][i2-1] = selection('Player1', letter_select)
    except IndexError:
        print('\tValor inválido, pierdes el turno')
        counter -= 1
    display_board(board)
    counter += 1
    
    if counter == 9:
        break
    
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] == '[O]' or board[i][0] == board[i][1] == board[i][2] == '[X]':
            victory = True
        if board[0][i] == board[1][i] == board[2][i] == '[O]' or board[0][i] == board[1][i] == board[2][i] == '[X]':
            victory = True
        
    if victory == True:
        print('\tGanó Jugador1')
        break
    
    if board[2][0] == board[1][1] == board[0][2] == '[O]' or board[0][0] == board[1][1] == board[2][2] == '[O]' or board[2][0] == board[1][1] == board[0][2] == '[X]' or board[0][0] == board[1][1] == board[2][2] == '[X]':
        print('\tGanó Jugador1')
        break
    
    i1 = 0
    try:
        player2 = catch(input('\tJugador2: '))
        while player2 >= 10:
            player2 -= 10
            i1 += 1
        i2 = player2
        if board[i1-1][i2-1] == '[O]' or board[i1-1][i2-1] == '[X]':
            print('\tValor inválido, pierdes el turno')
            counter -= 1
        else:
            board[i1-1][i2-1] = selection('Player2', letter_select)
    except IndexError:
        print('\tValor inválido, pierdes el turno')
        counter -= 1
    display_board(board)
    counter += 1
    
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] == '[O]' or board[i][0] == board[i][1] == board[i][2] == '[X]':
            victory = True
        if board[0][i] == board[1][i] == board[2][i] == '[O]' or board[0][i] == board[1][i] == board[2][i] == '[X]':
            victory = True
        
    if victory == True:
        print('\tGanó Jugador2')
        break
    
    if board[2][0] == board[1][1] == board[0][2] == '[O]' or board[0][0] == board[1][1] == board[2][2] == '[O]' or board[2][0] == board[1][1] == board[0][2] == '[X]' or board[0][0] == board[1][1] == board[2][2] == '[X]':
        print('\tGanó Jugador2')
        break
