import sys
try:

    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif sys.argv[1].find(".py") == -1:
        print("Not a python file")
        sys.exit(1)

    else:
        c=0
        with open(sys.argv[1]) as file:
            for line in file:
                if not line.lstrip().startswith("#") and not line.isspace():
                    c+=1
        print(c)


except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)