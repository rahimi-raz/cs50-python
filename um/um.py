import re
import sys

def main():
    print(count(input("Text: ").lower()))

def count(s):
    m=re.finditer(r"(\w*(um)\w*)",s,re.IGNORECASE)
    if m:
        c=0
        for i in m:
            if i.group().lower() == "um":
                c+=1
        return(c)
    else:
        return (0)

if __name__ == "__main__":
    main()