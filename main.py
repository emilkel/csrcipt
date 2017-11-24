import csv
import json
from pprint import pprint
import datetime



data = json.load(open('gett.json', encoding = "utf-8"))
#pprint(data)
#pprint(data['fields'][0])
#print(data['name:'])

with open("gett.csv", 'r', encoding = "utf-8", ) as csvfile:
    #csvfile = csv.reader (csvfile)
    for line in csvfile.readlines():
        array = line.split(',')
        first_item = array[0]
    num_columns = len(array)
    csvfile.seek(0)
    reader = csv.reader(csvfile)
    #data = list(reader)

    #included_cols = [0, 1, 2, 3, 4]
    #row_count = len(data)
    #print(row_count)
    column_names = [];
    row_count = sum(1 for row in reader)
    print(row_count)
    row_count += 2
    #for i  in range(0, row_count):
        #if ()
    csvfile.seek(0)
    rows = []
    nullable_arr =[]
    type_arr = []
    first_row = next(reader)
    with open("gett.csv", encoding = "utf-8") as csv_file:
        rows = [r for r in csv.reader(csv_file)]

    x=0
    print(rows)
    for i in range(0, row_count):
        content = first_row[i]
        for j in range (0, 15):
            if(data['fields'][j]['name'] == content):
                column_names.append(content)
                type_arr.append(data['fields'][j]['type'])
                if 'nullable' not in data['fields'][j]:
                    x+=1
                    nullable_arr.append(False)
                else:
                    nullable_arr.append(True)

                print("found " + content)
                #x += 1
                break
            #else:
                #print("1111")
print(nullable_arr)
print(column_names)
print(type_arr)
content_rows=[]
content_rows = rows[1:]
print(content_rows)
incor_null_rows = []
incorrect_null_rows = []


for i, elem in enumerate(content_rows):
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


        #for j in range(0,row_count):
         #   i

print("nullable", incorrect_null_rows)

incor_type_rows = []
incorrect_type_rows = []
datetime_object = 0
for i, elem in enumerate(content_rows):
        #print("i = " +str(i))
        #print("elem = " +str(elem[1]))
    for j in range(0,row_count):
        if (elem[j] and type_arr[j]=="StringType"):
            try:
                str(elem[j])
                incor_type_rows.append(True)
            except ValueError:
                incor_type_rows.append(False)
        elif(elem[j] and type_arr[j]=="TimestampType"):
            try:
                datetime_object = datetime.datetime.strptime(elem[j], "%Y-%m-%d %H:%M:%S+03")
                #print(datetime_object)
                incor_type_rows.append(True)
            except ValueError:
                incor_type_rows.append(False)
        else:
            #print("")
            try:
                int(elem[j])
                #print(elem[j])
                incor_type_rows.append(True)
            except ValueError:
                incor_type_rows.append(False)
    x = 0
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
    #print(incor_type_rows)
    incor_type_rows.clear()
print("type", incorrect_type_rows)
completed_row = incorrect_type_rows and incorrect_null_rows
print("complete", completed_row)

correct_rows = [r for r in rows[1:] if completed_row]
incorrect_rows = [r for r in rows[1:] if not completed_row]
print(correct_rows)
print(incorrect_rows)