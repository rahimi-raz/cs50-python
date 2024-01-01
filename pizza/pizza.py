from tabulate import tabulate
import sys
import csv
l=[]
try:

    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif sys.argv[1].find(".csv") == -1:
        print("Not a CSV file")
        sys.exit(1)

    else:
        with open(sys.argv[1]) as file:
            reader=csv.DictReader(file)
            # for i in reader:
            #     print(i)
            print(tabulate(reader,tablefmt="grid",headers="keys"))
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
