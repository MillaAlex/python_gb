"""Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч"""

MINIMUM = 0
MAXIMUM = 100000

num = int(input("Enter your number in range 0 - 100000: "))
counter = 0

if num < MINIMUM or num > MAXIMUM:
    print("The number exceeds the range. Enter other number.")
else:
    if num == 1:
        print("You've enetered 1.")
    if num > 1:
        for i in range(2, int(num**0.5 + 1)):
            if num % i == 0:
                counter += 1
        if counter > 0:
            print(f"The number {num} is compound.")
        else:
            print(f"The number {num} is prime.")
