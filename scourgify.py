import sys
import csv
import os
import os.path


def scourgify():
    nbr= len(sys.argv)
    if nbr <3:
        sys.exit('Too few command-line arguments')
    elif nbr >3:
        sys.exit('Too many command-line arguments')

    if sys.argv[1].endswith('.csv') and sys.argv[2].endswith('.csv') and nbr == 3:
        try:
            lines=[]
            with open(sys.argv[1],'r') as file1:
                reader = csv.reader(file1)
                next(reader) #and skip the first line because it is the title
                for row in reader:
                    name= row[0]
                    house = row[1]
                    last, first = name.split(', ')
                    lines.append({"first name": first, "last name": last, "house": house})

            with open(sys.argv[2],'w') as file2:
                writer2 = csv.DictWriter(file2, fieldnames=["first","last","house"])
                writer2.writeheader()
                for i in range(len(lines)):
                    writer2.writerow({"first": lines[i]["first name"], "last": lines[i]["last name"],"house": lines[i]["house"]})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
    elif sys.argv[1].endswith('.csv') == False or sys.argv[2].endswith('.csv') == False :
            sys.exit("Not a CSV file")


scourgify()
