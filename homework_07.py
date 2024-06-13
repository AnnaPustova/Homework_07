# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier * number <= 25:
        result = number * multiplier
        if result > 25:
            break
        print(f"{number} x {multiplier} = {result}")

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def number_addition(a,b):
    return a + b

print(number_addition(5,9))
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
print("Середнє арифметичне:", average(numbers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    return s[::-1]

input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Original string:", input_string)
print("Reverse string:", reversed_string)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(words):
    if not words:
        return ""

    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

words_list = ["apple", "banana", "cherry", "watermelon", "blueberry"]
print("The longest word is:", longest_word(words_list))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
        index = str1.find(str2)
        return index

print(find_substring("hello world", "world"))
print(find_substring("hello world", "python"))


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук

def count_friuts(apples):
    banana= apples * 4
    print(banana,apples)

count_friuts(4)
# task 8
#Порахуйте периметр фігури з task 05
# та виведіть його для користувача

def perimetery(a,b,c,d):
    return a + b+ c+ d

print(perimetery(5,15,30,85))
# task 9
"""Поиск слов Напишите функцию, которая принимает строку и число. 
Эта же функция находит массив, состоящий из слов, длина которых больше числа, переданного в функцию.
Я зашла на сайт практики по питон
"""

def words(n, str):
    length = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            length.append(x)
    return length
print(words(5, "Это обычная строка, в которой много слов"))
# task 10

"""Параметр по-умолчанию
Создайте функцию деления чисел, которая будет принимать три параметра. Сделайте последний параметр со значением по-умолчанию.
Вызовите функцию два раза:

с передачей третьего параметра
без передачи третьего параметра"""


def division(a, b, c=2):
    if b != 0 and c != 0:
        return a / b / c  # Если все не ноль
    else:
        print("Деление на ноль!")
    return a

print(division(23, 8))
print(division(100, 2, 5))