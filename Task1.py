a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
if a > b:
    if a // b >= 3:
        print('Больше чем в три раза')
    else:
        print('Больше')
else:
    print('Меньше')