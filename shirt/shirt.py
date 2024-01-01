import sys
from os.path import splitext
from PIL import Image, ImageOps
try:

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    type1=sys.argv[1].split(".")[1].lower()
    type2=sys.argv[2].split(".")[1].lower
    if type1 not in ("jpeg","jpg" ,"png") and type2 not in ("jpeg","jpg","png"):
        sys.exit("Not a jpeg file")

    try:
        t = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    size = shirt.size
    t = ImageOps.fit(t, size)
    # Paste shirt in muppet
    t.paste(shirt, shirt)
    t.save(sys.argv[2])
except (FileNotFoundError,IndexError):
    print("File does not exist")
    sys.exit(1)