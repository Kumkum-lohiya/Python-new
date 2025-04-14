lst = [1,2,3,4,5]
print(f'Before update {lst}')
lst[0] = "hello"
print(f'After update {lst}')

lst[0:3] = 10,20,30
print(lst)