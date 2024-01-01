import random
while True:
    try:
        n=int(input("level: "))
        if n<=0:
            raise ValueError
        while True:
            try:
                if n > 0 :
                    r=int(random.randint(0,n))
                    print(r)
                    g=int(input("Guess: "))
                    if g<0:
                        raise ValueError
                    if g>r:
                        print("Too Large!")
                    elif g<r:
                        print("Too Small!")
                    elif g==r:
                        print("Just Right!")
                        break
                else:
                    raise ValueError
            except ValueError:
                pass
    except ValueError:
        pass
    else:
        break

