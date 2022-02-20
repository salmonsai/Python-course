
import csv
import names

file_path = 'C:/Users/Sofa/Documents/python/lessons/CSV/'

csv_file_title = 'empty.csv'
file_title = file_path + csv_file_title
f = open(file_title, 'w')
f.close()

csv_file_title = 'digits.csv'
file_title = file_path + csv_file_title
with open(file_title, 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(0, 151):
        writer.writerow([i])

csv_file_title = 'names.csv'
file_title = file_path + csv_file_title
with open(file_title, 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(0, 100):
        writer.writerow([names.get_first_name()])

csv_file_title = 'emails.csv'
file_title = file_path + csv_file_title
with open(file_title, 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(0, 100):
        writer.writerow([names.get_first_name() + '@gmail.com'])


csv_file_title = 'nne.csv'
file_title = file_path + csv_file_title
with open(file_title, 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(0, 100):
        name = names.get_first_name()
        number = str(i)
        email = name + '@gmail.com'
        writer.writerow([number, name, email])
