
import names
import datetime
import random
from digits import digit
from name import name_first
from emails import email
from nne import nne_general
from combo import comb

file_path = 'C:/Users/Sofa/Documents/python/lessons/CSV/'

table_num = []
for i in range(10, 311):
    table_num.append({'Number': i})
digit(file_path, table_num)

table_name = []
for i in range(0, 401):
    table_name.append({'Names': names.get_first_name()})
name_first(file_path, table_name)

table_email = []
for i in range(0, 401):
    table_email.append({'Emails': names.get_first_name() + '@gmail.com'})
email(file_path, table_email)

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

nne_general(file_path, table_all)
comb(file_path, table_all)










