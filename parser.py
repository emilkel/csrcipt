import csv
import json
import datetime




def parse_csv(filepath: str) -> list:
    rows = []
    with open(filepath, encoding = "utf-8") as csv_file:
        rows = [r for r in csv.reader(csv_file)]
    return rows


def parse_format(filepath: str, all_rows: list) -> dict:

    data = json.load(open(filepath, encoding="utf-8"))
    column_names = [[] for i in range(3)]
    # не надо хардкодить значения (может быть больше 15 полей)
    for j in range(0, 15):                      
        column_names[0].append(data['fields'][j]['name'])
        # Следующие 4 строки можно поменять на column_names[1].append('nullable' in data['fields'][j])
        if 'nullable' not in data['fields'][j]:
            column_names[1].append(False)
        else:
            column_names[1].append(True)
        column_names[2].append(data['fields'][j]['type'])
    #"""Парсит файл с форматом и возвращает словарь"""
    return column_names


def check_header(header: list, fields: list) -> bool:

    row_count = sum(1 for row in header)
    # Почему 10?
    if (row_count < 10):
        print("there is not enough data")
        return False
    # if len(header) != len(dict):
    #   return False
    column_names = []
    print(row_count)
    for i in range(0, row_count):
        # if header[i] not in dict:
        #   return False
        for j in range(0, 15):
            # Не проверяется случай, когда в header'е больше полей, чем в формате
            if (fields[0][j] == header[i]):
                column_names.append(header[i])
                print("found " + header[i])
                break
    if len(column_names) < 10:
        return False
    """Проверяет, соответствует ли header формату"""
    return True


def check_nullable(row: list, fields: list) -> bool:

    row_count = len(fields[0])
    incor_null_rows = []
    incorrect_null_rows = []
    for i, elem in enumerate(row):
        for j in range(0, row_count):
            # В условии if не нужны скобки
            if (elem[j] == "" and fields[1][j] is True):
                incor_null_rows.append(True)
            elif (elem[j]):
                incor_null_rows.append(True)
            else:
                # incorrect_null_rows.append(False)
                # break
                incor_null_rows.append(False)
        # else:
        #   incorrect_null_rows.append(True)

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


    print("Check nullable:", incorrect_null_rows)

    """Проверяет, что пропущены только допустимые поля"""
    return incorrect_null_rows


def check_types(row: list, fields: list) -> bool:
    row_count = len(fields[0])
    incor_type_rows = []
    incorrect_type_rows = []
    for i, elem in enumerate(row):
        for j in range(0, row_count):
            if (elem[j] and fields[2][j] == "StringType"):
                try:
                    str(elem[j])
                    incor_type_rows.append(True)
                except ValueError:
                    incor_type_rows.append(False)
            elif (elem[j] and fields[2][j] == "TimestampType"):
                try:
                    datetime_object = datetime.datetime.strptime(elem[j], "%Y-%m-%d %H:%M:%S+03")
                    incor_type_rows.append(True)
                except ValueError:
                    incor_type_rows.append(False)
            else:
                try:
                    int(elem[j])
                    incor_type_rows.append(True)
                except ValueError:
                    incor_type_rows.append(False)
        x = 0
        length = len(incor_type_rows)
        while True:
            if (x >= length):
                incorrect_type_rows.append(False)
                incor_type_rows.clear()
                break
            else:
                if (incor_type_rows[x] == False):
                    x += 1
                else:
                    incorrect_type_rows.append(True)
                    incor_type_rows.clear()
                    break

    print("Check type: ", incorrect_type_rows)
    """Проверяет, что типы полей в строке соответствует полям в формате"""
    return incorrect_type_rows


# def parse(registry_path, format_path):
#   ...
#   return correct_rows, incorrect_rows

def main():
    all_rows = parse_csv("gett.csv")
    header = all_rows[0]
    rows = all_rows[1:]

    f = parse_format("gett.json", header)
    if not check_header(header, f):
        print("Wrong header!")
        return

    type = check_types(rows, f)
    nullable = check_nullable(rows, f)
    completed_row = type and nullable
    print("Completed rows:", completed_row)

    correct_rows = [r for r in rows if completed_row]
    incorrect_rows = [r for r in rows if not completed_row]

    print("Corrected rows: ", correct_rows)
    print("Incorrected rows: ", incorrect_rows)



if __name__ == '__main__':
    main()
