age = int(input("Enter your age = "))
if(age >= 18 and age <101):
    print('you can vote')
elif age >= 101:
    print("greater than 101")
elif age <=0 :
    print("invalid age ")