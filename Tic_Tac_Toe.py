#Создайте программу для игры в ""Крестики-нолики""

print('Добро пожаловать в игру крестики - нолики!')

field = list(range(1,10))

def Get_Field(field):
    print('=' * 13)
    for i in range(3):
        print('|', field[0+i*3], '|', field[1+i*3], '|', field[2+i*3], '|')
        print('=' * 13)

def Get_Input(player):
    val = False
    while not val:
        answer = input("Куда ходим " + player+"? ")
        try:
            answer = int(answer)
        except:
            print('Введите число!')
            continue
        if answer >= 1 and answer <= 9:
            if(str(field[answer - 1]) not in 'XO'):
                field[answer - 1] = player
                val = True
            else:
                print('Место занято!')
        else:
            print('Введите число от 1 до 9!')

def Winner(field):
    field_place = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in field_place:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[0]
    return False

def Game(field):
    place = 0
    win = False
    while not win:
        Get_Field(field)
        if place % 2 == 0:
            Get_Input('X: ')
        else:
            Get_Input('O: ')
        place += 1
        if place > 4:
            temporary = Winner(field)
            if temporary:
                print(temporary, 'Победитель!')
                win = True
                break
        if place == 9:
            print('Ничья!')
            break
    Get_Field(field)
Game(field)

input('Нажмите ввод.')