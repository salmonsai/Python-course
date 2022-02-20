import csv


def comb(file_path, table_all):
    csv_file_title = 'combo.csv'
    file_title = file_path + csv_file_title
    table_all.sort(key=lambda x: x['Name'])

    with open(file_title, 'w', newline='') as f:
        field = ['Number', 'Name', 'Email', 'Date', 'Phone', 'Gender', 'Salary']
        writer = csv.DictWriter(f, fieldnames=field)
        writer.writeheader()
        writer.writerows(table_all)
