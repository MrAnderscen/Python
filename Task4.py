import math
import random

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def arccos(num):
    return math.acos(num)

while (True):  ##начало цикла



 operation = input("Введите символ операции (+, -, /, *, ^, mod, rand, !, acos,exit): ")

 if operation == "+": ##сложение
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 + num2
    print("Результат: ", result)
 elif operation == "-": ##вычитание
     num1 = float(input("Введите первое число: "))
     num2 = float(input("Введите второе число: "))
     result = num1 - num2
     print("Результат: ", result)
 elif operation == "/":##деление
     num1 = float(input("Введите первое число: "))
     num2 = float(input("Введите второе число: "))
     if num2 == 0:
        print('Делить на ноль нельзя')
     result = num1 / num2
     print("Результат: ", result)
 elif operation == "*":##умножение
     num1 = float(input("Введите первое число: "))
     num2 = float(input("Введите второе число: "))
     result = num1 * num2
     print("Результат: ", result)
 elif operation == "^":##возведение в степень
     num1 = float(input("Введите число: "))
     power = float(input("Введите степень: "))
     result = num1 ** power
     print("Результат: ", result)
 elif operation == "mod":##остаток от деления
     num1 = float(input("Введите число: "))
     mod = float(input("Введите делитель: "))
     result = num1 % mod
     print("Результат: ", result)
 elif operation == "rand":##рандомизация из диапозона
     low = float(input("Введите нижнюю границу диапазона: "))
     high = float(input("Введите верхнюю границу диапазона: "))
     result = random.uniform(low, high)
     print("Результат: ", result)
 elif operation == "!":##факториал
     num = int(input("Введите число для вычисления факториала: "))
     result = factorial(num)
     print("Результат: ", result)
 elif operation == "acos":##арккосинус
     num = float(input("Введите число для вычисления арккосинуса: "))
     result = arccos(num)
     print("Результат: ", result)
 elif operation == "exit":##Выход из цикла при надобности
     break
 else:
     print("Неверный символ операции")