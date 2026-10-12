# learners.py
# Responsible for learner registration, searching and profile management
from Validation import validate_name,validate_age,validate_learner_id

students=[]

def register_learner():
    student={}
    try:
     student_id=int(input("Enter the Student's ID: "))
     student_name=input("Enter the name of the student: ").title()
     student_age=int(input("Enter the student's age: "))
    except ValueError:
        print("Student_id and student_age should be a poitive  integer.Please try again.")
    else:
        student={
            "student_id": student_id,
            "name": student_name,
            "age": student_age
        }
    if (validate_learner_id(student["student_id"],students) and validate_name(student["name"])and validate_age(student["age"])):
           students.append(student)
    return "Registration Error.Try again"
def validate_learner_data(student):

    if (
        student["student_id"] > 0
        and student["name"].strip() != ""
        and student["name"].replace(" ", "").isalpha()
        and 6 <= student["age"] <= 12
    ):
        return True

    return False



def learner_exists():
   try:
       search_id=int(input("Enter the student's ID: "))
   except ValueError:
       print("Student ID must be an integer.")
       return
   found = False
   for student in students:
       if search_id==student["student_id"]:
           print(f"{student['student_id']},found")
           found=True
           break
   if not found:
           print("Student is not in the system.")

def find_learner():
    try:
        search_id=int(input("Enter the student's ID: "))
    except ValueError:
        print("The Student ID should be an integer")
        return
    found=False
    for student in students:
        if search_id==student["student_id"]:
            print(f"Student ID: {student['student_id']}\n")
            print(f"Name: {student['student_name']}\n")
            print(f"Age: {student['student_age']}\n")
            found=True
            break
    if not found:
            print("Student is not registered yet.")
    
def update_learner():
    try:
        update_id=int(input("Enter the student's ID: "))
    except ValueError:
        print("Student's ID should be an integer.")
        return
    found=False
    for student in students:
        if update_id==student["student_id"]:
            try:
              student["student_age"]=int(input("Enter student's Age: "))
            except ValueError:
                print("Update ID should be an integer.")
            else:
             print("Age update successfully.")
             found=True
             break
    if not found:
            print("Student not registered yet.Try again")
def get_learner_profile():
    try:
     profile_id=int(input("Enter the student id for the student: "))
    except ValueError:
            print("Profile ID should be an Integer.Try again")
            return
    found=False
    for student in students:
         if profile_id==student["student_id"]:
             print(f"Student ID: {student['student_id']}\n")
             print(f"Name: {student['student_id']}\n")
             print(f"Age: {student['student_age']}\n")
             found=True
             break
    if not found:
         print("Student does not exist in the System.Try again!")

