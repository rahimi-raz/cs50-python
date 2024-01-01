def main():
    x=input("enter division: ")
    r=convert(x)
    if r not in ("ZeroDivisionError" , "ValueError"):
        print(gauge(r))

def convert(x):
    while True:
        try:
            x,y=x.split('/')
            if int(y)==0 :
                raise ZeroDivisionError
            elif int(x)>int(y) or int(x) < 0 or int(y) < 0:
                raise ValueError
            v=round(int(x)*100 / int(y))
            return v
        except (ValueError,ZeroDivisionError):
            raise

def  gauge(v):
    if v>=99 :
        return 'F'
    elif v<= 1:
        return 'E'
    else:
        return (f"{v}%")


if __name__ == "__main__":
    main()



