# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F
score=int(input("enter the mark scored:" ))
if score>=90: 
    print("Grade A")
elif score>=80:
    print("Grade B")
elif score>=70:
    print("Grade C")
elif score>=60:
    print("Grade D")
elif score>=40:
    print("Grade E")
else :
    score<40
    print("Grade F")
    
    