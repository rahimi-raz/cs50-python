def say_hello(greeting):
    #print(greeting," ",greeting[0])
    if greeting == 'hello':
        print("$0")
    elif greeting[0] == 'h':
        print("$20")
    else:
        print("$100")

def main():
    greeting = input("say greeting please: ").strip().lower().split(" ")
    #print(greeting[0][:5])
    say_hello(greeting[0][:5])
main()