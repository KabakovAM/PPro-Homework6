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


def riddles(check):
    puzzles = {'В Полотняной стране\nПо реке Простыне\nПлывет пароход\nТо назад, то вперед,\nА за ним такая гладь —\nНи морщинки не видать.\n':
               ['утюг', 'Утюг', 'iron', 'Iron'],
               'В синем небе светляки —\nНе дотянешь к ним руки.\nА один большой светляк\nИзогнулся, как червяк.':
               ['звёзды', 'месяц', 'Звёзды', 'Месяц']}
    for key, item in puzzles.items():
        print(riddle(key, item, check))


if __name__ == '__main__':
    check = 10
    riddles(check)