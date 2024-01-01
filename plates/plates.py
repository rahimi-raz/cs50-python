def main():
    inpt=input("enter plates:")
    print(isvalid(inpt))

def isvalid(inp):
    if   2 > len(inp)  or len(inp) > 6 or inp[0] == '0':
        #print("lengh error")
        return "invalid"
    else:
        for i in range(len(inp)):
            if not inp[i].isnumeric() and not inp[i].isalpha():
                return "invalid"
            elif inp[i].isnumeric() and inp[len(inp)-1].isalpha():
                return "invalid"
            elif i < (len(inp)-1) and  inp[i].isnumeric() and inp[i+1].isalpha():
                return "invalid"
            elif inp[i] == '0' and not inp[i-1].isnumeric():
                return "invalid"
        return "valid"
main()

