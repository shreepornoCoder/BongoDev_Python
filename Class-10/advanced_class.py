class Result:
    def __init__(self, math_marks, science_marks):
        self.math_marks = math_marks
        self.science_marks = science_marks

    def get_average(self):
        return (self.math_marks + self.science_marks) / 2
    
student1 = Result(71, 89)
print(student1.get_average())