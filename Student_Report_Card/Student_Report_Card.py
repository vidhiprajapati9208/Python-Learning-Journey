print("Welcome to Student Report Card")
name = input("Enter Student Name: ")
Roll_Number = int(input("Enter Student Roll Number: "))

marks = {}
English = int(input("Enter English Marks: "))
marks.update({"English": English})
Maths = int(input("Enter Maths Marks: "))
marks.update({"Maths": Maths})
Science = int(input("Enter Science Marks: "))
marks.update({"Science": Science})

Total_marks = English + Maths + Science
Average_marks = Total_marks / 3
print("========== STUDENT REPORT CARD ==========")
print("Student Name: ",name)
print("Roll Number: ", Roll_Number)
print("English Marks: ",English)
print("Maths Marks: ",Maths)
print("Science Marks: ",Science)
print("Total Marks: ",Total_marks)
print("Average Marks: ",Average_marks)

if (Average_marks >= 90):
    print("Grade: A")
elif(Average_marks >= 80):
    print("Grade: B")
elif(Average_marks >= 70):
    print("Grade: C")
elif(Average_marks >= 60):
    print("Grade: D") 
else:
    print("Grade: Fail")



print("=========================================")