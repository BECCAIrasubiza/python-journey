def average_age(ages):
    total_age = sum(ages)
    average = total_age / len(ages)
    return average

def female_students(class_list):
    female_students = []
    
    for student in class_list:
        if student[1] == "Female":
            female_students.append(student[0])
            count=len(female_students)
            
    return female_students,count
def male_students(class_list):
    male_students = []
    for student in class_list:
        if student[1] == "Male":
            male_students.append(student[0])
    return male_students
class_list = [
    ["Rebecca Irasubiza", "Female", "10"],
    ["Ineza Joan", "Female", "12"],
    ["Rwigamba Patrick", "Male", "8"],
    ["Ntacyabukura Levi", "Male", "17"],
    ["Iragena Tabitha", "Female", "14"]
]
ages = []

class_students = {
    "names": ["Rebecca Irasubiza", "Ineza Joan", "Rwigamba Patrick", "Ntacyabukura Levi", "Iragena Tabitha"],
    "gender": ["Female", "Female", "Male", "Male", "Female"],
    "age": ["10", "12", "8", "17", "14"]
}

#for student in class_list:
   #ages.append(int(student[2]))
#print("average age of all students:", average_age(ages))
#print(f"female students: {female_students(class_list)[0]}, Count: {female_students(class_list)[1]}")
#print(f"male students: {male_students(class_list)}")
for student in class_list:
    print(f"student: {student[0]}")