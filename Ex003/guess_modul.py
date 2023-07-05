from random import randint
from sys import argv

def guess(start, stop, check):
    num = randint(start, stop)
    while check != 0:
        data = int(input('Введите число: '))
        if data == num:
            return True
        if data < num:
            print('Больше!')
        else:
            print('Меньше!')
        check -= 1
    return False

if __name__ == '__main__':
    start, stop, check = (int(i) for i in argv[1:])
    print(guess(start, stop, check))