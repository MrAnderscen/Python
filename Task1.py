a = int(input())
b = int(input())
if a > b:
    if a // b >= 3:
        print('More than three times')
    else:
        print('High')
else:
    print('Low')