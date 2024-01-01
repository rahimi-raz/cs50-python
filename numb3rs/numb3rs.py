import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    maches=re.search(r"^(\d\d?\d?)\.(\d\d?\d?)\.(\d\d?\d?)\.(\d\d?\d?)", ip)
    if maches:
        a,b,c,d=maches.groups()
        if 0<= int(a) <=255 and 0<= int(b) <=255 and 0<= int(c) <=255 and 0<= int(d) <=255 and ip.count(".")==3 and len(ip.split("."))==4:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()

