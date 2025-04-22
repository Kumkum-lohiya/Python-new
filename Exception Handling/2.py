try:
    file = open('D:\2nd year\python\online\Exception Handling\errors.txt')
    content = file.read()
    print(content)

except FileNotFoundError:
    print('File not Found')

finally:
    file.close()
    print('file operation completed ')
