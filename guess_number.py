"""Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации 
случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)"""

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
TRIES = 10

from random import randint

num = randint(LOWER_LIMIT, UPPER_LIMIT)
counter = 0
while TRIES > counter:
    guessed_num = int(input("Enter your num from 0 to 1000: "))
    if guessed_num == num:
        print("Correct. Good job!")
    elif guessed_num > num:
        print("Too big. Try again.")
        TRIES -= 1
    elif guessed_num < num:
        print("Too small. Try again.")
        TRIES -= 1
    if TRIES == 0:
        print("You've run out of tries.")
        break
    