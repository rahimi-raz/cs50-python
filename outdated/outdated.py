import re
mo=[
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]

while True:
    try:
        inp=input("date: ")
        c=inp.find(",")

        m,d,y=inp.replace("/"," ").replace(","," ").split()
        if m in mo and c==-1:
            raise ValueError
        if m not in mo and int(m)>12 or int(d)>31:
            raise ValueError
    except ValueError:
        pass
    else:
        if m in mo:
            m=str(mo.index(m)+1)
        d=d.zfill(2) if len(d)==1 else d
        m=m.zfill(2) if len(m)==1 else m
        print (y,m,d,sep="-")
        break
# f"{m:02}
