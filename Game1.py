
def input_data(area_size):
    main_input = []
    for i in range(area_size):
        sub_input = []
        main_input.append(sub_input)
        for j in range(area_size):
            sub_input.append('-')
    return main_input


def output(data):
    symbols = "abcdefghijklmnopqrstuvwxyz"
    # выводит буквы сверху
    print('  ', end=' ')
    for h in range(x):
        print(symbols[h], end=' ')
    print()
    print(' ', '--' * x)
    # выводит номер строки и строку матрицы
    for h, r in enumerate(data):
        print(str(h) + '|', *r)


def moves(data):
    symbols = "abcdefghijklmnopqrstuvwxyz"
    check = input('Твой ход(укажи клетку в формате "a0"): ')
    value = input('Укажи значение(x,o): ')
    # Разделяем значения на букву и цифру
    check_one = symbols.find(check[0])
    check_two = int(check[1])
    data[check_two][check_one] = value


def condition(data):
    main_diagonal = []
    second_diagonal = []
    horizontals_verticals = []
    for i in range(len(data)):
        sub_verticals = []
        sub_horizontals = []
        horizontals_verticals.append(sub_verticals)
        horizontals_verticals.append(sub_horizontals)
        main_diagonal.append(data[i][i])  # главная диагональ
        second_diagonal.append(data[i][(len(data) - 1) - len(second_diagonal)])  # второстепенная диагональ
        for j in range(len(data)):
            sub_verticals.append(data[j][i])  # запись вертикали
        for h in range(len(data)):
            sub_horizontals.append(data[i][h])  # запись горизонтали

    if len(set(main_diagonal)) == 1 and '-' not in main_diagonal:
        print('Ты выиграл по главной диагонали')
        return True
    elif len(set(second_diagonal)) == 1 and '-' not in main_diagonal:
        print('Ты выиграл по второй диагонали')
        return True
    for r in horizontals_verticals:
        if len(set(r)) == 1 and '-' not in r:
            print('Игрок выиграл')
            return True
    return False

x = int(input('Введите размерность поля: '))
data2 = input_data(x)

while True:
    output(data2)
    moves(data2)
    if condition(data2):
        break
