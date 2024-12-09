student = {"name":"Shreeporno", "roll":55, "grade":9}
student2 = {"school":"HCPSC"}

student.update(student2)

print(student)

new = {**student, **student2}
print(new) 

new.clear()
print(new)