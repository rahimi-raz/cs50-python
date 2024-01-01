inp=input("enter your twitt: ")
t=""
for i in inp:
    if i in ("U","O","I","E","A","i","o","u","e","a"):
        t += ""
    else:
        t+=i
print(t)
