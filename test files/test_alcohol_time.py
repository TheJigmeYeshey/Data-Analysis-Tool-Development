import os
import csv
import re

def retrieve_data():

    selected_data = []

    with open("victoria_accident.csv", "r") as file:
        reader = csv.reader(file)
        headers = next(reader)

        for row in reader:
            date_parts = row[4].split('/')

            date_value = int(date_parts[2] + date_parts[1])

            if row[6] == 'Yes':
                selected_data.append(row)

    return selected_data


def test_alcohol_time():

    selected_data = retrieve_data()

    for data in selected_data:
        assert data[6] == 'Yes'

