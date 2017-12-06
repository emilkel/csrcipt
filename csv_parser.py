import csv
import json
import datetime
import glob

def parse_csv(filepath: str) -> list:
    rows = []
    with open(filepath, encoding = "utf-8") as csv_file:
        rows = [r for r in csv.reader(csv_file)]
    return rows


def parse_format(filepath: str, all_rows: list) -> dict:

    data = json.load(open(filepath, encoding="utf-8"))
    column_names = [[] for i in range(3)]
    col_number = len(data['fields'])
    column_dict = dict()
    for i in range(0, len(all_rows)):
        for j in range(0, col_number):
            if (data['fields'][j]['name'] == all_rows[i]):
                column_dict[data['fields'][j]['name']] =['nullable' in data['fields'][j],data['fields'][j]['type']]
    """Парсит файл с форматом и возвращает словарь"""
    return column_dict


def check_header(header: list, fields: dict) -> bool:

    row_count = sum(1 for row in header)
    fields_count = len(fields)
    column_names = []
    for key, value in fields.items():
        for i in range(0, row_count):
            if key == header[i]:
                break
        else:
            return False
    """Проверяет, соответствует ли header формату"""
    return True


def check_nullable(row: list, fields: dict) -> bool:

    row_count = len(fields)
    incorrect_null_rows = []
    for i, elem in enumerate(row):
        j = - 1
        for key,value in fields.items():
            j += 1
            if (elem[j] == "" and value[0] is False):
                incorrect_null_rows.append(False)
                break
        else:
            incorrect_null_rows.append(True)

    print("Check nullable:", incorrect_null_rows)

    """Проверяет, что пропущены только допустимые поля"""
    return incorrect_null_rows


def check_types(row: list, fields: dict) -> bool:
    row_count = len(fields)
    incorrect_type_rows = []
    for i, elem in enumerate(row): #движемся по строкам
        j=-1 #счетчик для столбцов (быдло код, не знаю как по другому)
        for key, value in fields.items(): #движемся по словарю
            j+=1
            #print(isinstance(elem[j], int), fields[2][j],elem[j],"\t")
            if (elem[j] and value[1] == "IntegerType"):

                try:
                    int(elem[j])
                except ValueError:
                    incorrect_type_rows.append(False)
                    break
#"%Y-%m-%d %H:%M:%S+03"

            elif (elem[j] and value[1] == "TimestampType"):
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
    #C:\Users\TDInstaller\Desktop\files
    path = r'C:\Users\TDInstaller\Desktop\files'
    allFiles = glob.glob(path + "/*.csv")
    for i in range (0, len(allFiles)):
        parse_file = allFiles[i]
        all_rows = parse_csv(parse_file)
        header = all_rows[0]
        rows = all_rows[1:]
        f = parse_format("gett.json", header)
        if not check_header(header, f):
            print("Wrong header!")
            return
        correct_rows = []
        incorrect_rows = []
        type = check_types(rows, f)
        nullable = check_nullable(rows, f)
        completed_row = [nullable[i]and type[i] for i in range(len(nullable))]
        print("Completed rows:", completed_row)
        #print(len(completed_row))
        for r in range(0, len(completed_row)):
            if completed_row[r]:
                correct_rows.append(rows[r])
            else:
                incorrect_rows.append(rows[r])

        #correct_rows = [r for r in rows if completed_row]
        #incorrect_rows = [r for r in rows if not completed_row[r]==True] #вот это почему то не работает
        print("Corrected rows: ", correct_rows)
        print("Incorrected rows: ", incorrect_rows)
        print("\n\n")





if __name__ == '__main__':
    main()




