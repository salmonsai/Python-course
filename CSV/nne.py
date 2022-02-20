import csv


def nne_general(file_path, table_all):
    csv_file_title = 'nne_2.csv'
    file_title = file_path + csv_file_title
    with open(file_title, 'w', newline='') as f:
        field = ['Number', 'Name', 'Email', 'Date']
        writer = csv.DictWriter(f, fieldnames=field)
        writer.writeheader()
        for i in table_all:
            writer.writerow({k: v for k, v in i.items() if k in field})
