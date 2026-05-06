#RushiL Mohamed
#Write a Python program using if–elif–else ladder to assign grades: ≥ 80: A Grade, 60–79: B Grade, 50–59: C Grade, < 50: Fail
mark = int(input("Marks:"))

if marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")