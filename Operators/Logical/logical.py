"""
multiple conditions combine - Boolean True/False

and -all conditions must be true > True
or - at least one condition True
not - single operand, reverse
"""
age = 20
is_student = True
print(age>18 and is_student)
print(age >25 or is_student)
print(not is_student)

print('\n')

a = 10
b =20
print(a>5 and b >10)
print(a<1 or b==20)
print(not(a== 10))