#yield keyword
def generator(num):
    while num >0:
        yield num # yield values one at a time
        num -= 1


#using the generator
for number in generator(5):
    print(number)

# generator(4)
# print(generator)