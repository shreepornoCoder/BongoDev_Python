num = int(input("Enter Your Average Mark: "))
grade = ''

if num >= 90:
    grade = 'A+'

elif num < 90 and num >= 70:
    grade = 'A-'

elif num < 70 and num >= 50:
    grade = 'B'

else:
    grade = 'Fail'

print(f"Your Grade is {grade}")