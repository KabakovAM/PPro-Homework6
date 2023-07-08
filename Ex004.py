def riddle(puzzle, answer, check):
    print(f'Загадка:\n\n{puzzle}')
    count = 1
    while count <= check:
        data = input('Введите ответ загадки: ')
        if data in answer:
            return count
        else:
            count += 1
    return 0

if __name__ == '__main__':
    puzzle = 'В Полотняной стране\nПо реке Простыне\nПлывет пароход\nТо назад, то вперед,\nА за ним такая гладь —\nНи морщинки не видать.\n'
    answer = ['утюг', 'Утюг', 'iron', 'Iron']
    check = 10
    print(riddle(puzzle, answer, check))