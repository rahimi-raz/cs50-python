def main():
    word=input("enter your twitt: ")
    print(shorten(word))
#   return shorten()

def shorten(word):

    t=""
    for i in word:
        if i in ("U","O","I","E","A","i","o","u","e","a"):
            t += ""
        else:
            t+=i
    return(t)

if __name__ == "__main__":
    main()