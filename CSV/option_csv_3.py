import csv
import names
import datetime
import random

file_path = 'C:/Users/Sofa/Documents/python/lessons/CSV/'

table_all = []
gender_list = ['male', 'female']
for i in range(0, 1000):
    number = str(i)
    name = names.get_first_name()
    email = name + '@gmail.com'
    date = datetime.datetime.now()
    if i <= 50:
        time = date.replace(year=random.randint(1980, 1990))
    elif 50 < i <= 150:
        time = date.replace(year=random.randint(1991, 2000))
    elif 150 > i <= 300:
        time = date.replace(year=random.randint(2001, 2010))
    else:
        time = date.replace(year=random.randint(2011, 2021))

    phone = random.randint(10**11, 9*10**11)
    gender = gender_list[random.randint(0, 1)]
    salary = str(random.randint(100, 1000)) + ' usd'

    table_all.append({'Number': number,
                      'Name': name,
                      'Email': email,
                      'Date': time,
                      'Phone': phone,
                      'Gender': gender,
                      'Salary': salary
                      })

csv_file_title = 'nne_3.csv'
file_title = file_path + csv_file_title
with open(file_title, 'w', newline='') as f:
    field = ['Number', 'Name', 'Email', 'Date']
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()
    for n in range(0, 450):
        writer.writerow({k: v for k, v in table_all[n].items() if k in field})

ff = open(file_title, 'r')
reader = list(csv.DictReader(ff, fieldnames=['Number', 'Name', 'Email', 'Date']))
ff.close()
# print(len(reader))

table_new = []
for i in table_all:
    i.pop('Number')

for i in reader:
    email = names.get_last_name() + '@ya.ru'
    phone = random.randint(10 ** 11, 9 * 10 ** 11)
    gender = gender_list[random.randint(0, 1)]
    salary = str(random.randint(100, 1000)) + ' usd'
    table_new.append({'Name': i['Name'],
                      'Email': email,
                      'Date': i['Date'],
                      'Phone': phone,
                      'Gender': gender,
                      'Salary': salary})

csv_file_title = 'combo.csv'
file_title = file_path + csv_file_title
table_combo = table_new + table_all[450:1000]
table_combo.sort(key=lambda x: x['Name'])

with open(file_title, 'w', newline='') as f:
    field = ['Name', 'Email', 'Date', 'Phone', 'Gender', 'Salary']
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()
    writer.writerows(table_combo)

