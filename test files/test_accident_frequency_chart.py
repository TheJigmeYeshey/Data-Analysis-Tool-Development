import os
import csv
import re

def retrieve_data(selected_start_date, selected_end_date, hour):

    start_date = int(selected_start_date.split('/')[1] + selected_start_date.split('/')[0])
    end_date = int(selected_end_date.split('/')[1] + selected_end_date.split('/')[0])

    selected_data = []

    with open("victoria_accident.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            hour_value = row[5].split('.')[0]
            date_parts = row[4].split('/')

            date_value = int(date_parts[2] + date_parts[1])

            if hour_value == hour and start_date <= date_value <= end_date:
                selected_data.append(row)

    date_hour = {}

    for row in selected_data:

        key = row[4]

        if key in date_hour:
            date_hour[key] += 1
        else:
            date_hour[key] = 1

    sorted_dates = sorted(date_hour.keys(), key=lambda x: (int(x.split('/')[2]), int(x.split('/')[1]), int(x.split('/')[0])))

    return sorted_dates

def test_alcohol_chart():

    selected_start_date = "07/2013"
    selected_end_date = "08/2013"
    hour = '03'

    sorted_dates = retrieve_data(selected_start_date, selected_end_date, hour)

    for date in sorted_dates:
        matching_rows = [row for row in retrieve_data(selected_start_date, selected_end_date, hour) if row[4] == date]
        assert all(row[5].split('.')[0] == '03' for row in matching_rows), f"Hour is not '03' for date {date}"
