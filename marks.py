#Rushil Mohamed
#Write a Python program using if–elif–else ladder to assign grades: ≥ 80: A Grade 60–79: B Grade 50–59: C Grade < 50: Fail
marks = int(input("Marks: "))
if marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Result: Fail")