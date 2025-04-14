"""
in -True/False
not in - opposite
"""
lst_1 =[1,2,3,4,5]
check = int(input('Enter a number to check : '))
# if check in lst_1:
#     print('Found')
# else:
#     print('Not Found')

if check not in lst_1:
    print('Not Found')
else:
    print('Found')