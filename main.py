import csv
import json
from pprint import pprint



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
    first_row = next(reader)
    x = 0
    for i in range(0, row_count):
        content = first_row[i]
        for j in range (x, 15):
            if(data['fields'][j]['name'] == content):
                column_names.append(content)
                print("found " + content)
                #x += 1
                break
            #else:
                #print("1111")

print(column_names)
#print(first_row[i])

       # print(row)
       # content = row[0]
       # print(row[0])
       # if (data['fields'][0]['name'] == content):
        #    print("!!!")
        #print(content)

    #for row in reader:
     #   content = next(reader)
            #print(content)
#   print(data['fields'][0]['name'])
    #print(content)    print()

       # print(content[0])
        #print(content[1])
