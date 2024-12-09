from icecream import ic

student = {"name":"Shreeporno",
           "roll":55,
           "grade":9}

ic(student)
ic(student["grade"])
ic(student.get("roll", "Not Found"))

student["school"] = "HCPSC" # adding new key-value
student['grade'] = 10 # updating value
ic(student)

# print(student.popitem()) # removing the last item
# ic(student)

del student['roll']
ic(student)