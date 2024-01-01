def convert(inp):
    inp=inp.replace(":)" , "🙂")
    inp=inp.replace(":(" , "🙁")
    return inp


def main():
    inpt=input("enter input: ")
    print(convert(inpt))
main()