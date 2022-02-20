import csv


def digit(file_path, table_num):
    csv_file_title = 'digits_2.csv'
    file_title = file_path + csv_file_title
    with open(file_title, 'w', newline='') as f:
        field = ['Number']
        writer = csv.DictWriter(f, fieldnames=field)
        writer.writeheader()
        writer.writerows(table_num)
