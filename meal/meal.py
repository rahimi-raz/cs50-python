def convert(time):
    h,m=time.split(":")
    m=int(str(int(m)/60 *100).split('.')[0])
    #print(str(int(m)/60))
    time=h+"."+str(m)
    time=float(time)
    #print("{:.1f}".format(time))
    return time

def main():
    time=input("please input a time: ").strip()
    time = float(convert(time))
    #print(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13 :
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()