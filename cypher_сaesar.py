alphabet_eng = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

while True:
    print("Код операций: шифрование - '1', дешифрование - '2'")
    operation = input('Введите код операции: ')
    if operation != '1' and operation != '2':
        print('Такой операции не существует. Попробуйте ещё раз!')
        continue

    language = input('Выберите язык "rus" или "eng": ')
    alphabet = ''
    if language == 'eng':
        alphabet = alphabet_eng
    elif language == 'rus':
        alphabet = alphabet_rus
    else:
        print('Язык введен некорректно. Поробуйте еще раз!')
        continue

    rotate = int(input('Введите шаг сдвига: '))
    if rotate < 1 or rotate > len(alphabet) // 4:
        print(f'Шаг сдвига должен быть в диапазоне [1, {len(alphabet) // 4}]. Попробуйте ещё раз!')
        continue

    text = input('Введите исходный текст: ')

    ind = 0
    if operation == '1':
        for i in text:
            if i in alphabet:
                text = text[:ind] + alphabet[alphabet.find(i) + rotate] + text[ind + 1:]
            ind += 1
    elif operation == '2':
        for j in text:
            if j in alphabet:
                text = text[:ind] + alphabet[alphabet.rfind(j) - rotate] + text[ind + 1:]
            ind += 1

    print(text)

    restart = input('Выполним ещё операцию? ')
    if restart.lower() == 'да':
        pass
    else:
        print('До свидания!')
        break