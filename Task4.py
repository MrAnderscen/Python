import math
import random

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def arccos(num):
    return math.acos(num)

operation = input("Введите символ операции (+, -, /, *, ^, mod, rand, !, acos): ")

if operation == "+":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 + num2
    print("Результат: ", result)
elif operation == "-":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 - num2
    print("Результат: ", result)
elif operation == "/":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    if num2 == 0:
        print('Делить на ноль нельзя')
    result = num1 / num2
    print("Результат: ", result)
elif operation == "*":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 * num2
    print("Результат: ", result)
elif operation == "^":
    num1 = float(input("Введите число: "))
    power = float(input("Введите степень: "))
    result = num1 ** power
    print("Результат: ", result)
elif operation == "mod":
    num1 = float(input("Введите число: "))
    mod = float(input("Введите делитель: "))
    result = num1 % mod
    print("Результат: ", result)
elif operation == "rand":
    low = float(input("Введите нижнюю границу диапазона: "))
    high = float(input("Введите верхнюю границу диапазона: "))
    result = random.uniform(low, high)
    print("Результат: ", result)
elif operation == "!":
    num = int(input("Введите число для вычисления факториала: "))
    result = factorial(num)
    print("Результат: ", result)
elif operation == "acos":
    num = float(input("Введите число для вычисления арккосинуса: "))
    result = arccos(num)
    print("Результат: ", result)
else:
    print("Неверный символ операции")