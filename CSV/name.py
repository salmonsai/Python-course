import csv


def name_first(file_path, table_name):
    csv_file_title = 'names_2.csv'
    file_title = file_path + csv_file_title
    with open(file_title, 'w', newline='') as f:
        field = ['Names']
        writer = csv.DictWriter(f, fieldnames=field)
        writer.writeheader()
        writer.writerows(table_name)
