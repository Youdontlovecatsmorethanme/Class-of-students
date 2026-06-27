import csv

class StudentInfo:
    def __init__(self, name, age, gpa, city):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.city = city
    def to_list(self):
        return [self.name, self.age, self.gpa, self.city]

print("Enter student details")
Name = input("Enter name:")
Age = input("Enter age:")
Gpa = input("Enter gpa:")
City = input("Enter city:")
new_student = StudentInfo(Name, Age, Gpa, City)

with open('student_data.csv', 'w', newline='') as csvfile:
    writer =csv.writer(csvfile)
    writer.writerow(new_student.to_list())
