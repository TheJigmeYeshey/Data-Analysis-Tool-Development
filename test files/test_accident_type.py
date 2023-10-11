import os
import csv
import re

def accident_type():

    types = []

    with open("victoria_accident.csv", "r") as file:
        reader = csv.reader(file)
        headers = next(reader)

        for row in reader:
            accident_type = row[7]
            types.append(accident_type)

    return(types)


def test_accident_type():

    with open("victoria_accident.csv", "r") as file:
        reader = csv.reader(file)
        headers = next(reader)

        types = accident_type()

        for type in types:

            assert type in ['Struck Pedestrian', 'Collision with vehicle', 'Collision with a fixed object', 'No collision and no object struck', 'Struck animal', 'Vehicle overturned (no collision)', 'collision with some other object', 'Fall from or in moving vehicle', 'Other accident']




