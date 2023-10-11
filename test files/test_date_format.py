import os
import csv
import re
import csv


def read_csv_file(file_path):
    data = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                data.append(row)
    return data


def test_formatted_date():
    file_name = "victoria_accident.csv"

    data = read_csv_file(file_name)

    for row in data:
        date = row[4]
        date_components = date.split('/')
        if len(date_components) == 3:
            formatted_date = f"{date_components[1]}/{date_components[2]}"
            assert re.match(r'\d{1,2}/\d{4}', formatted_date) is not None
