import random

word_list = ['земля', 'астероид', 'звезда', 'спутник', 'галактика', 'нептун', 'комета', 'метеорит',
             'компьютер', 'телевизор', 'кондиционер', 'чайник', 'бойлер', 'холодильник', 'микроволновка', 'тостер',
             'жираф', 'дельфин', 'медведь', 'тигр', 'кенгуру', 'кит', 'барсук', 'волк',
             'окена', 'река', 'озеро', 'море', 'залив', 'пруд', 'лиман', 'канал',
             'полицейский', 'судья', 'мэр', 'президент', 'депутат', 'инспектор', 'губернатор', 'министр']

category = ['Космический объект', 'Бытовая техника',  'Млекопитающее', 'Водоём', 'Госслужащий']

def get_word():
    res = random.choice(word_list)
    return res.upper()

def display_hangman(tries):
    stages = [
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            _
        ''',
        '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     /
        _
        ''',
        '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     
        _
        ''',
        '''
        --------
        |      |
        |      O
        |     \\|
        |      |
        |     
        _
        ''',
        '''
        --------
        |      |
        |      O
        |      |
        |      |
        |     
        _
        ''',
        '''
        --------
        |      |
        |      O
        |      
        |      
        |     
        _
        ''',
        '''
        --------
        |      |
        |      
        |      
        |      
        |     
        _
        ''',
        '''
        
        |      
        |      
        |      
        |      
        |     
        _
        ''',
        '''
        
              
              
              
              
             
        
        '''
    ]
    return stages[tries]

eng = 'abcdefghijklmnopqrstuvwxwz'

def play(text):
    print('Давайте играть в угадайку слов!')
    print('1 - Легко, 2 - Сложно')
    while True:
        complexity = int(input('Введите уровень сложности (1 или 2): '))
        if complexity != 1 and complexity != 2:
            print('Такого уровня сложности нету! Попробуйте еще раз')
            continue
        else:
            break
    word_completion = '_' * len(text)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    if complexity == 1:
        tries = 8
        word_completion = text[0] + word_completion[1:len(word_completion)-1] + text[-1]
    id_category = 0
    if text.lower() in word_list[0:8]:
        id_category = 0
    elif text.lower() in word_list[8:16]:
        id_category = 1
    elif text.lower() in word_list[16:24]:
        id_category = 2
    elif text.lower() in word_list[24:32]:
        id_category = 3
    elif text.lower() in word_list[32:]:
        id_category = 4
    print(display_hangman(tries))
    print(word_completion, f'Категория: {category[id_category]}', sep='  ')

    while guessed is False:
        print(f'Названные буквы: {guessed_letters}, слова: {guessed_words}')
        new_letter = input('Введите букву или слово: ').upper()
        if new_letter == text:
            guessed = True
        elif new_letter.lower() in eng:
            print('Ошибка! Используйте русские буквы.')
            continue
        elif new_letter.isalpha():
            pass
        else:
            print('Ошибка! Нужно ввести букву.')
            continue

        if new_letter in guessed_letters:
            print('---------------------------------------------------------------------------------------------------')
            print(display_hangman(tries))
            print(word_completion, f'Категория: {category[id_category]}', sep='  ')
            print(f'Вы ранее называли букву {new_letter}')
            continue
        elif new_letter in guessed_words:
            print('---------------------------------------------------------------------------------------------------')
            print(display_hangman(tries))
            print(word_completion, f'Категория: {category[id_category]}', sep='  ')
            print(f'Вы ранее называли слово {new_letter}')
            continue
        elif len(new_letter) == 1:
            guessed_letters.append(new_letter)
        else:
            guessed_words.append(new_letter)

        if new_letter == text:
            pass
        elif new_letter in text:
            ind = 0
            for i in text:
                if i == new_letter:
                    word_completion = word_completion[:ind] + i + word_completion[ind + 1:]
                ind += 1
            print('---------------------------------------------------------------------------------------------------')
            print(display_hangman(tries))
            print(word_completion, f'Категория: {category[id_category]}', sep='  ')
        else:
            tries -= 1
            print('---------------------------------------------------------------------------------------------------')
            print(display_hangman(tries))
            print(word_completion, f'Категория: {category[id_category]}', sep='  ')

        if word_completion == text:
            guessed = True

        if guessed is True:
            print('Поздравляем, вы угадали слово! Вы победили!')

        if tries == 0:
            print(f'Вы проиграли! Загаданное слово: {text}')
            break


while True:
    word = get_word()
    play(word)
    restart = input('Сыграем ещё раз? ')
    if restart.lower() == 'да':
        pass
    else:
        print('Спасибо за игру. До свидания!')
        break