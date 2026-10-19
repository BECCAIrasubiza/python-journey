
from student import Student

print(type(50))                         # <class 'int'>
print(type("hello"))                    # <class 'str'>
print(type([]))                         # <class 'list'>
print(type({}))                         # <class 'dict'>
print(type(Student("Harry", "Gryffindor")))   # <class 'student.Student'>

# str has methods just like our class does: "hello".upper() is a method call
# on a str object, the same way student.charm() is a method call on a Student.
print("hello".upper())
