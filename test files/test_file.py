import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def test_read_victoria_accident_csv():
    file = "victoria_accident.csv"
    data = read_csv_file(file)
    assert len(data) > 0
