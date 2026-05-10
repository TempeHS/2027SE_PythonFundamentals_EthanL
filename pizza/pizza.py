import sys
import csv
import os
from tabulate import tabulate

# check number of arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

# Check file
if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

# check file existence
if not os.path.isfile(filename):
    sys.exit("File does not exist")

rows = []

with open(filename) as file:
    reader = csv.reader(file)
    for row in reader:
        rows.append(row)

print(tabulate(rows, tablefmt="grid"))
