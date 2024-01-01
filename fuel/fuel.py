while True:
    try:
        x=input("enter division: ")
        x,y=x.split('/')
        if int(x)>int(y):
            raise ValueError
        v=round(int(x)*100 / int(y))
        if v>=99 :
            print('F')
        elif v<= 1:
            print('E')
        else:
            print(v,"%",sep="")
    except(ValueError,ZeroDivisionError):
        pass
    else:
        break

