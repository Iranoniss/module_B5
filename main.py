board = [' ' for x in range(9)]

def print_board(): #выводит поле для игры
    row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
    row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
    row3 = f"| {board[6]} | {board[7]} | {board[8]} |"

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon): # Ход игрока
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2

    print("Твоя очередь, игрок {}".format(number))
    choice = int(input("Введите свой ход (1-9): ").strip())
    if board[choice - 1] == ' ': #вставить значение Х или О
        board[choice - 1] = icon
    else:
        print()
        print("Это место уже занято!")

def is_victory(icon): #Выигрышные варианты или условия победы
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw(): #Ничья или победа того или иного игрока
    if ' ' not in board:
        return True
    else:
        return False
    while True:
        print_board()
        player_move('X')
        print_board()
        if is_victory('X'):
            print(" X Победил! Поздравляем!")
            break
        elif is_draw():
            print("Это ничья!")
            break
        player_move('O')
        if is_victory('O'):
            print_board()
            print(" O Победил! Поздравляем!")
            break
        elif is_draw():
            print("Это ничья!")
            break


