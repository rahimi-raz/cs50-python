inpt=input("please enter your mathematic expressions: ").strip()
number1,cal,number2=inpt.split(' ')
#print(number1,'__',cal,'__',number2)
if cal not in ("+" , "*" , "/" , "-"):
    print("please enter correct calcuation sign")
elif not(number1.isnumeric()) or not(number2.isnumeric()):
    print("please enter digit")
else:
    match cal:
        case "+":
            res = float(number1)+float(number2)
            print(f"{res:.1f}")
        case "-":
            res = float(number1)-float(number2)
            print(f"{res:.1f}")
        case "*":
            res = float(number1)*float(number2)
            print(f"{res:.1f}")
        case "/":
            res = float(number1)/float(number2)
            print(f"{res:.1f}")