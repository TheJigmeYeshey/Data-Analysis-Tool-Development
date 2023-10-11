import os
import csv
import re

def data_dictionary(selected_data):

    type_counts = {}

    for row in selected_data:
        type = row[7]
        if type in type_counts:
            type_counts[type] += 1
        else:
            type_counts[type] = 1

    return type_counts


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

    type_counts = data_dictionary(selected_data)

    return type_counts

def test_frequency_type_chart():

    selected_start_date = "07/2013"
    selected_end_date = "08/2013"

    type_counts = retrieve_data(selected_start_date, selected_end_date)

    valid_types = ['Struck Pedestrian', 'Collision with vehicle', 'Collision with a fixed object', 'No collision and no object struck', 'Struck animal', 'Vehicle overturned (no collision)', 'Collision with some other object', 'Fall from or in moving vehicle', 'Other accident']

    for type in type_counts:
        assert type in valid_types