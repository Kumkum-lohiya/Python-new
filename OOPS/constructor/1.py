class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade


student1 = Student('Kumkum',23,'A++')
student2 = Student('Khushal',20,'A+++')


print(student1.name,student1.age,student1.grade)
print(student2.name,student2.age,student2.grade)


"""
1 - default constructor(self)
2 - parameterized constructor(self,name,age)
3 - constructor with default values (self, name = "unknown")
"""