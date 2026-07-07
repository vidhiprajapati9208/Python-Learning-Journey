grades = ("A", "B", "A", "C", "A")
print("number of 'A' grades: ", grades.count("A"))

top_students = []
name1 = input("Enter name :")
name2 = input("Enter name :")
name3 = input("Enter name :")
top_students = [name1, name2, name3]
print("original student list: " , top_students)

top_students.insert(1, "Pending Review")
top_students.sort()
print("sorted list: ", top_students)

print("Popped Element:", top_students.pop())

print("Final List:", top_students)
print("Final Length:", len(top_students))



