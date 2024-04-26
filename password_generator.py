import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous_symbols = 'il1Lo00'
chars = ''

quantity_passwords = int(input('Количество паролей? '))
len_password = int(input('Длина пароля? '))
presence_digits = input('Включать цифры в пароль? ')
up_letters = input('Включать прописные буквы? ')
low_letters = input('Включать строчные буквы? ')
presence_punctuation = input('Включать символы пунктуации? ')
exclude_ambiguous_symbols = input('Исключать однозначные символы? ')


if presence_digits.lower() == 'да' or presence_digits.lower() == 'yes':
    chars += digits
if up_letters.lower() == 'да' or up_letters.lower() == 'yes':
    chars += uppercase_letters
if low_letters.lower() == 'да' or low_letters.lower() == 'yes':
    chars += lowercase_letters
if presence_punctuation.lower() == 'да' or presence_punctuation.lower() == 'yes':
    chars += punctuation
if exclude_ambiguous_symbols.lower() == 'да' or exclude_ambiguous_symbols.lower() == 'yes':
    for i in chars:
        if i in ambiguous_symbols:
            chars = chars.replace(i, '')

def generate_password(length_password, alphabet):
    res = ''
    for _ in range(length_password):
        res += random.choice(alphabet)
    return res

for i in range(quantity_passwords):
    if chars == '' or len_password == 0:
        print('Вы исключили все символы. Пароли не сгенерируются!')
        break
    new_password = generate_password(len_password, chars)
    print(new_password)