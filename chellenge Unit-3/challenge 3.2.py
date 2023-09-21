class student:
  
   def __init__(self, name, roll_number, cgpa):
     self.name=name
     self.roll_number=roll_number
     self.cgpa=cgpa

def sort_students(student_list):
  sorted_students= sorted(student_list, key=lambda student: 
                                  student.cgpa, reverse=True)

  return sorted_students                        

students = [
    student("Alice","A101",7.8),
    student("Bob","B102",8.9),
    student("charlie","C103",9.1),
    student("David","D104",9.9),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))