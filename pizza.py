import sys
import csv
from tabulate import tabulate

def table():
    nbr=len(sys.argv)
    if nbr < 2:
        sys.exit('Too few command-line arguments')
    elif nbr > 2:
         sys.exit('Too many command-line arguments')
    elif sys.argv[1].endswith('.csv')==False:
         sys.exit('Not a CSV file')

    try:
         with open(sys.argv[1]) as file:
            data = []
            reader = csv.DictReader(file)
            for line in reader:
                data.append([line[reader.fieldnames[0]], line[reader.fieldnames[1]], line[reader.fieldnames[2]]])
            print(tabulate(data, reader.fieldnames, tablefmt="grid"))
    except FileNotFoundError:
         sys.exit('File does not exist')

table()
