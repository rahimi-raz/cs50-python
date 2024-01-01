import inflect
p = inflect.engine()
mylist = p.join(("apple", "banana", "carrot"))
l=[]
#print(type(mylist))
while True:

    try:
        n=input("Name: ")
        l.append(str(n))
    except EOFError:
        print("Adieu, adieu, to",p.join(l))
        break