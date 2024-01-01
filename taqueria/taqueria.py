food={
"Baja Taco": 4.00,
"Burrito": 7.50,
"Bowl": 8.50,
"Nachos": 11.00,
"Quesadilla": 8.50,
"Super Burrito": 8.50,
"Super Quesadilla": 9.50,
"Taco": 3.00,
"Tortilla Salad": 8.00
}
p=0
while True:
	try:
		inp=input("food: ").title()
		p+=round(food[inp],2)
		print("total:$%.2f" % p , sep="")
	except KeyError:
		pass
	except EOFError:
		break



