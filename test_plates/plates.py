def main():
    inpt=input("enter plates:")
    print(is_valid(inpt))

def is_valid(inp):
    if   2 > len(inp)  or len(inp) > 6 or inp[0] == '0':
        #print("lengh error")
        return False
    else:
        for i in range(len(inp)):
            if not inp[i].isnumeric() and not inp[i].isalpha():
                return False
            elif inp[i].isnumeric() and inp[len(inp)-1].isalpha():
                return False
            elif i < (len(inp)-1) and  inp[i].isnumeric() and inp[i+1].isalpha():
                return False
            elif inp[i] == '0' and not inp[i-1].isnumeric():
                return False
            elif  inp[0].isalpha() == False or inp[1].isalpha() == False:
                return False
        return True
if __name__ == "__main__":
    main()

