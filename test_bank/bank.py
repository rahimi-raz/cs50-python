def value(greeting):
    if greeting == 'hello':
        return(0)
    elif greeting[0] == 'h':
        return(20)
    else:
        return(100)

def main():
    greeting = input("say greeting please: ").strip().lower().split(" ")
    res=value(greeting[0][:5])
    print(f"${res}")

if __name__ == "__main__":
    main()