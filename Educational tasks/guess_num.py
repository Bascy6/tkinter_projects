from random import *
"""Угадай число"""
def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100

def guess_num(count, num):
    n = input('\nВведите целое число от 1 до 100 включительно: ')

    if is_valid(n) is False:
        print('\nА может быть все-таки введем целое число от 1 до 100?')
        return guess_num(count, num)
    else:
        n = int(n)
        if n < num:
            print('\nВаше число меньше загаданного, попробуйте еще разок')
            count += 1
            return guess_num(count, num)
        elif n > num:
            print('\nВаше число больше загаданного, попробуйте еще разок')
            count += 1
            return guess_num(count, num)
        else:
            print('\nВы угадали, поздравляем!')
            count += 1
            print(f'Количество попыток: {count}')
            answer = input('\nСыграем ещё раз?\n')
            if answer == 'Да':
                count = 0
                num_new = randint(1, 100)
                print('\nЗагадано новое число.')
                return guess_num(count, num_new)

    return '\nСпасибо, что играли в числовую угадайку. Еще увидимся...'

num = randint(1, 100)
tries = 0
print('Добро пожаловать в числовую угадайку')
print(guess_num(tries, num))