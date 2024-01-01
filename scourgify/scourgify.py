import sys
import csv
d={}
try:

    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif sys.argv[1].find(".csv") == -1:
        print("Not a CSV file")
        sys.exit(1)

    else:
        with open(sys.argv[1]) as file:
            reader=csv.DictReader(file)
            with open(sys.argv[2] , "w") as file2:
                writer=csv.DictWriter(file2,fieldnames=["first", "last","house"])
                writer.writeheader()
                for i in reader:
                    last=i["name"].split(",")[0].strip()
                    first=i["name"].split(",")[1].strip()
                    writer.writerow({"first":first , "last":last , "house": i["house"]})
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)