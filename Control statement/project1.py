num1 = float(input("Enter first number = "))
num2 = float(input("Enter second number = "))

choice =input("Enter your choice + ,-,*,/,//,%,** = ")
if choice == '+':
    print(num1+num2)
elif choice == '-':
    print(num1-num2)
elif choice == '*':
    print(num1*num2)
elif choice == '/':
    print(num1/num2)
elif choice == '**':
    print(num1**num2)
elif choice == '%':
    print(num1%num2)
elif choice == '//':
    print(num1//num2)
else:
    print("invalid choice")
