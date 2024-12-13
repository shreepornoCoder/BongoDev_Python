class Student:
    def __init__(self, name, roll):
        self.name = name # property
        self.roll = roll

stu1 = Student("Shreeporno", 9) # object

print(stu1.name, stu1.roll)