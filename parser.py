import csv
import json





def parse_csv(filepath: str) -> list:
    rows = []
    with open(filepath, encoding = "utf-8") as csv_file:
        rows = [r for r in csv.reader(csv_file)]

    return rows


def parse_format(filepath: str, all_rows: list) -> dict:

    data = json.load(open(filepath, encoding="utf-8"))
    column_names = []
    for j in range(0, 15):
        column_names.append(data['fields'][j]['name'])
    print(column_names)
    #"""Парсит файл с форматом и возвращает словарь"""
    return {'fields': column_names}


def check_header(header: list, fields: list) -> bool:

    row_count = sum(1 for row in header)
    if (row_count < 10):
        print("there is not enough data")
        return False
    column_names = []
    print(row_count)
    for i in range(0, row_count):
        for j in range(0, 15):
            if (fields[j] == header[i]):
                column_names.append(header[i])
                print("found " + header[i])
                break
    if len(column_names) < 10:
        return False
    """Проверяет, соответствует ли header формату"""
    return True

'''
def check_nullable(row: list, fields: list) -> bool:

    incor_null_rows = []
    incorrect_null_rows = []
    for i, elem in enumerate(row):
        #print("i = " +str(i))
        #print("elem = " +str(elem[1]))
        for j in range(0,row_count):
            if (elem[j]=="" and nullable_arr[j] is True):
                incor_null_rows.append(True)
                #print("row is correct")
            elif(elem[j]):
                incor_null_rows.append(True)
                #print("row is correct")
            else:
                incor_null_rows.append(False)
                #print("row is not correct")

    #print(incor_rows)
    x = 0
    length = len(incor_null_rows)
    while True:
        if (x >= length):
            incorrect_null_rows.append(True)
            incor_null_rows.clear()
            break
        else:
            if (incor_null_rows[x] == True):
                x += 1
            else:
                incorrect_null_rows.append(False)
                incor_null_rows.clear()
                break

    """Проверяет, что пропущены только допустимые поля"""
    return True


def check_types(row: list, fields: dict) -> bool:
    """Проверяет, что типы полей в строке соответствует полям в формате"""
    return True


def correct_row(row: list, fields: dict) -> bool:
    return check_nullable(row, fields) and check_types(row, fields)
'''

def main():
    all_rows = parse_csv("gett.csv")
    #print(all_rows)
    header = all_rows[0]
    rows = all_rows[1:]

    f = parse_format("gett.json", header)
 #   check_nullable(rows, header)

    if not check_header(header, f['fields']):
        print("Wrong header!")
        return
    '''
    correct_rows = [r for r in rows if correct_row(r, f['fields'])]
    incorrect_rows = [r for r in rows if not correct_row(r, f['fields'])]

    print(correct_rows)
    print(incorrect_rows)

'''

if __name__ == '__main__':
    main()
