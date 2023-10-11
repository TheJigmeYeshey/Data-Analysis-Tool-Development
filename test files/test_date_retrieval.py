import os
import csv
import re

def retrieve_data(selected_start_date, selected_end_date):

    start_date = int(selected_start_date.split('/')[1] + selected_start_date.split('/')[0])
    end_date = int(selected_end_date.split('/')[1] + selected_end_date.split('/')[0])

    selected_data = []

    with open("victoria_accident.csv", "r") as file:
        reader = csv.reader(file)
        headers = next(reader)

        for row in reader:

            date_parts = row[4].split('/')

            date_value = int(date_parts[2] + date_parts[1])

            if start_date <= date_value <= end_date:
                selected_data.append(row)

    return selected_data

def test_retrieve_data():
    selected_start_date = "7/2013"
    selected_end_date = "8/2013"

    selected_data = retrieve_data(selected_start_date, selected_end_date)

    assert len(selected_data) > 0
