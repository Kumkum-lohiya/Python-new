"""
burger - function
extra cheese - extra feature

main function > function add
without changing the main function code
"""
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called ")
        func()
        print("Somthing is happening before the function is called ")
    return wrapper()

@my_decorator
def say_hello():
    print("Hello")


say_hello()