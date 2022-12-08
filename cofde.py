
first= int(input("enter first number :"))
operator = input("enter operator (+,-,*,/%) :")
second = int(input("enter second number :"))
if operator== "+" :
    print("your anser is",first + second)
elif operator== "-":
    print("your anser is",first-second)
elif operator=="*":
    print("your anser is",first*second)
elif operator=="/":
    print("your anser is",first/second)
elif operator=="%":
    print("your anser is",first%second)
elif operator== "//":
    print("your anser is",first//second)
else:
    print("enter enter valid operator")
