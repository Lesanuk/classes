
class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1 # to keep on track of students

student1 = Student("Spongebob", 30)
student2 = Student("Patrik", 35)
student3 = Student("Sandy", 27)
student4 = Student("Mahi", 25)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

