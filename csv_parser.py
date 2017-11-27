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
    col_number = len(data['fields'])
    for i in range(0, len(all_rows)):
        for j in range(0, col_number):
            if (data['fields'][j]['name'] == all_rows[i]):
                column_names[0].append(data['fields'][j]['name'])
                column_names[1].append('nullable' in data['fields'][j])
                column_names[2].append(data['fields'][j]['type'])
    print("column:", column_names)
    #"""Парсит файл с форматом и возвращает словарь"""
    return column_names


def check_header(header: list, fields: list) -> bool:

    row_count = sum(1 for row in header)
    column_names = []
    print(row_count)
    for i in range(0, row_count):
        for j in range(0, 15):
            if (fields[0][j] == header[i]):
                column_names.append(header[i])
                print("found " + header[i])
                break
    """Проверяет, соответствует ли header формату"""
    return True


def check_nullable(row: list, fields: list) -> bool:

    row_count = len(fields[0])
    incor_null_rows = []
    incorrect_null_rows = []
    for i, elem in enumerate(row):
        for j in range(0, row_count):
            #print(fields[1][j])
            if (elem[j] == "" and fields[1][j] is False):
                incorrect_null_rows.append(False)
                break
        else:
            incorrect_null_rows.append(True)

    print("Check nullable:", incorrect_null_rows)

    """Проверяет, что пропущены только допустимые поля"""
    return incorrect_null_rows


def check_types(row: list, fields: list) -> bool:
    row_count = len(fields[0])
    incor_type_rows = []
    incorrect_type_rows = []
    for i, elem in enumerate(row):
        for j in range(0, row_count):
            #print(isinstance(elem[j], int), fields[2][j],elem[j],"\t")
            if (elem[j] and fields[2][j] == "IntegerType"):
                try:
                    int(elem[j])
                except ValueError:
                    incorrect_type_rows.append(False)
                    break
#"%Y-%m-%d %H:%M:%S+03"

            elif (elem[j] and fields[2][j] == "TimestampType"):
                try:
                    datetime_object = datetime.datetime.strptime(elem[j], "%Y-%m-%d %H:%M:%S+03")
                except ValueError:
                    incorrect_type_rows.append(False)
                    break
        else:
            incorrect_type_rows.append(True)
    print("Check type: ", incorrect_type_rows)
    """Проверяет, что типы полей в строке соответствует полям в формате"""
    return incorrect_type_rows


def main():
    parse_file = "test2.csv"
    #file_par = input()
    all_rows = parse_csv(parse_file)
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




