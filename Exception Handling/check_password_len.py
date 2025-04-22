# check password length
def check_password(password):
    if len(password) < 8:
        raise Exception('Error : Password must be >= 8 characters')
    print('Password is strong')

try:
    password = input('enter a password = ')
    check_password(password)
except Exception as e:
    print(e)