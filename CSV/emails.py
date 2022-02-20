import csv


def email(file_path, table_email):
    csv_file_title = 'emails_2.csv'
    file_title = file_path + csv_file_title
    with open(file_title, 'w', newline='') as f:
        field = ['Emails']
        writer = csv.DictWriter(f, fieldnames=field)
        writer.writeheader()
        writer.writerows(table_email)
