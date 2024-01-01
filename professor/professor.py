import random
import sys

def main():
    n=get_level()
    while True:
        try:
            score=0
            for i in range(10):
                a=generate_integer(n)
                b=generate_integer(n)
                for j in range(3):
                    try:
                        x=int(input(f"{a} + {b} = "))
                        if x == sum([a,b]):
                            score+=1
                            break
                        elif x!=sum([a,b]) and j!=2:
                            print("EEE")
                        elif j==2:
                            print(sum([a,b]))
                    except ValueError:
                        print("EEE")
                        if j==2:
                            print(sum([a,b]))
                print("total: " , score)

        except ValueError:
            pass
        else:
            sys.exit(0)


def get_level():
    while True:
        try:
            n=input("Level: ")
            if n not in ("1","2","3"):
                raise ValueError
        except ValueError:
            pass
        else:
            return int(n)

def generate_integer(n):
        r=[None] * 10
        if int(n)==1:
            return random.randint(0,9)
        elif int(n)==2:
            return random.randint(10,99)
        else:
            return random.randint(100,999)




if __name__ == "__main__":
    main()

