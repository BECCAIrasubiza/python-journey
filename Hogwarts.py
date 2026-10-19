students=["becca","james","Tabitha","jane"]

houses=["Kayonza","Kayonza","Kayonza","Rwamaya"]
#print(students[0])
#print(students[1])
#print(students[2])
#print(students[3])

#for student in students:
    #print(student)
for i in range(len(students)):
    print(i+1, students[i])

students={
    "becca": "Kayonza",
    "james": "Kayonza",
    "Tabitha": "Kayonza",
    "jane": "Rwamaya"
}
print(students["becca"])
print(students["james"])
print(students["Tabitha"])
print(students["jane"])

for student in students:
    print(student, students[student], sep=",")


students=[
    {"name":"becca", "house":"Kayonza", "patronus":"cat"},
    {"name":"james", "house":"Kayonza", "patronus":"dog"},
    {"name":"Tabitha", "house":"Kayonza", "patronus":"rabbit"},
    {"name":"jane", "house":"Rwamaya", "patronus":None}
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=",")