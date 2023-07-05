from random import randint

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
    print(guess(12, 50, 10))