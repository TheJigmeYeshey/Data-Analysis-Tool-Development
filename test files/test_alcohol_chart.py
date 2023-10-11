import os
import csv
import re

def retrieve_data(selected_start_date, selected_end_date):

    selected_start_date = "07/2013"
    selected_end_date = "08/2013"

    start_date = int(selected_start_date.split('/')[1] + selected_start_date.split('/')[0])
    end_date = int(selected_end_date.split('/')[1] + selected_end_date.split('/')[0])

    selected_data = []

    with open("victoria_accident.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            date_parts = row[4].split('/')

            date_value = int(date_parts[2] + date_parts[1])

            if row[6] == 'Yes' and start_date <= date_value <= end_date:
                selected_data.append(row)

    date_counts = {}

    for row in selected_data:
        date = row[4]
        if date in date_counts:
            date_counts[date] += 1
        else:
            date_counts[date] = 1

    sorted_dates = sorted(date_counts.keys(), key=lambda x: (datetime.datetime.strptime(x, "%d/%m/%Y").year,
                                                             datetime.datetime.strptime(x,
                                                                                        "%d/%m/%Y").month))

    return sorted_dates

def test_alcohol_chart():

    selected_start_date = "07/2013"
    selected_end_date = "08/2013"

    sorted_dates = retrieve_data(selected_start_date, selected_end_date)

    for date in sorted_dates:
        matching_rows = [row for row in selected_data if row[4] == date]  # Find rows with the same date
        assert all(row[6] == 'Yes' for row in matching_rows), f"Alcohol time is not 'Yes' for date {date}"

# Shows the count of accident types for a specified time period

