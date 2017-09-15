import csv


def get_csv_data(filename):
    # create an empty list of rows
    rows = []
    # open the CSV file
    data_file = open(filename, "r")
    # create a CSV Reader from a CSV file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
