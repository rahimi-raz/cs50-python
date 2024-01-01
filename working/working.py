import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    matches=re.search(r"^(\d\d?):?(\d\d?)? (AM|PM) to (\d\d?):?(\d\d?)? (PM|AM)",s)
    if matches:
        p=matches.groups()
        if p[1] and int(p[1])>=60 or p[4] and int(p[4]) >=60:
            raise ValueError
        if int(p[0]) > 12 or int(p[3]) > 12:
            raise ValueError
        part1=set_format(p[0],p[1],p[2])
        part2=set_format(p[3],p[4],p[5])
        return part1 + " to " + part2
    else:
        raise ValueError


def set_format(h, m, ap):
    if ap == 'PM':
        if int(h) == 12:
            new_h = 12
        else:
            new_h = int(h) + 12
    else:
        if int(h) == 12:
            new_h = 0
        else:
            new_h = int(h)
    if m == None:
        time = f"{new_h:02}" + ":00"
    else:
        time = f"{new_h:02}" + ":" + m
    return time







if __name__ == "__main__":
    main()