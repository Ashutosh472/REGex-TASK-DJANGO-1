english = float(input(" Please enter English Marks: "))
math = float(input(" Please enter Math score: "))
computers = float(input(" Please enter Computer Marks: "))
physics = float(input(" Please enter Physics Marks: "))
chemistry = float(input(" Please enter Chemistry Marks: "))

total = english + math + computers + physics + chemistry
percentage = (total / 500) * 100

print("Total Marks = %.2f"  %total)
print("Marks Percentage = %.2f"  %percentage)

if(percentage >= 90):
    print("A Grade")
    print("QUALIFIED FOR SCHOLARSHIP")
elif(percentage >= 80):
    print("B Grade")
    print("QUALIFIED FOR SCHOLARSHIP")
elif(percentage >= 70):
    print("C Grade")
    print("QUALIFIED FOR SCHOLARSHIP")
elif(percentage >= 60):
    print("D Grade")
    print("NOT QUALIFIED FOR SCHOLARSHIP")
elif(percentage >= 40):
    print("E Grade")
    print("NOT QUALIFIED FOR SCHOLARSHIP")
else:
    print("Fail”)
