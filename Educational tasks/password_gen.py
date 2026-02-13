from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = digits + lowercase_letters + uppercase_letters + punctuation

count = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите длину одного пароля: '))

digit = input('Включать ли цифры 0123456789 (y/n)? ')
upper = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ (y/n)? ')
lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz (y/n)? ')
punct = input('Включать ли символы !#$%&*+-=?@^_ (y/n)? ')
ambigous = input('Исключать ли неоднозначные символы il1Lo0O (y/n)? ')

if digit == 'n':
    chars -= digits
if upper == 'n':
    chars -= uppercase_letters
if lower == 'n':
    chars -= lowercase_letters
if punct == 'n':
    chars -= punctuation
if ambigous == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += choice(chars)
    
    return password

for i in range(count):
    print(f'{i+1}-й пароль: {generate_password(length, chars)}')