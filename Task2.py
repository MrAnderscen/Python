string = input("Введите строку: ")
for i in range(len(string)): ##проверка на длину строки и на букву с
    if i == 2: 
        continue
    elif string[i] == "c": 
         print("Найден символ \'c\'!")
print(string[i]) 
print("Длина строки:", len(string)) 
print("Строка без последнего символа:", string[:-1])