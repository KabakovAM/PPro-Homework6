from sys import argv
_data_dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:31, 12:31}

def data_check(data: list):
    data_list = list(map(int, data[0].split('.')))
    if data_list[1] in _data_dic and 1 <= data_list[2] <= 9999:
        if data_list[1] == 2 and leap_year(data_list[2]) and 1 <= data_list[0] <= 29:
            return True
        elif 1 <= data_list[0] <= _data_dic[data_list[1]]:
            return True
    return False

def leap_year(year):
    if year % 400 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    elif year % 4 == 0:
        result = True
    else:
        result = False
    return result

if __name__ == '__main__':
    data = argv[1:]
    print(data_check(data))