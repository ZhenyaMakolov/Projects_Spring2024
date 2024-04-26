import random

print('Добро пожаловать в числовую угадайку')
right_border = int(input('Укажите правую границу: '))
num = random.randint(1, right_border)

def is_valid(x):
    try:
        x = int(x)
        if 1 <= x <= right_border:
            return True
    except:
        return False

attempts = 0

while True:
    number = input(f'Введите число от 1 до {right_border}: ')
    if is_valid(number):
        number = int(number)
        if number < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            attempts += 1
        elif number > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            attempts += 1
        else:
            print('Вы угадали, поздравляем!')
            attempts += 1
            print(f'Вы угадали с {attempts} попыток')
            restart_game = input('Сыграем еще раз?: ')
            if restart_game.lower() == 'да':
                right_border = int(input('Укажите правую границу: '))
                num = random.randint(1, right_border)
                attempts = 0
            else:
                print('Спасибо, что играли в числовую угадайку! Еще увидимся...')
                break
    else:
        print(f'А может быть все-таки введем целое число от 1 до {right_border}?')