
sum=0
while True:
    inp=input("Insert Coin: ")
    if inp in ("5" , "10", "25"):
        sum+= int(inp)
    if (50-sum) > 0:
        print("Amount Due:", abs(sum-50))
    else:
        print("Change Owed:", abs(sum-50))
        break


