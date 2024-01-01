students=[]
# with open("student.csv") as file:
#     for l in file:
#         row=l.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")
#-----------------------------------------------------------
with open("student.csv") as file:
    for l in file:
        name,house=l.rstrip().split(",")
        student={"name": name,"house":house}
        students.append(student)
for i in students:
    print(f"{i['name']} is in {i['house']}")

#-----------------------------------------------------------

students = []
with open("student.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
