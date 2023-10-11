import os
import csv
import re

def accident_hour():
    hours = []
    with open("victoria_accident.csv", "r") as file:
        reader = csv.reader(file)
        headers = next(reader)

        for row in reader:
            hour_value = row[5].split('.')[0]
            hours.append(hour_value)

    return hours


def test_accident_hour():
    hours = accident_hour()
    valid_hour_values = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

    for hour in hours:
        assert hour in valid_hour_values







