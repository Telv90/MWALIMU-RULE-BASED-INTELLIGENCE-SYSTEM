# validation.py
# Responsible for validating user input
# NB string manipulation methods e.g isdigit(),isalpha(),title(),split(),strip() works for strings only.

# Validate_name checks wether the name provided is a valid name,not empty.
def validate_name(name):
    if name.strip()=="":
        return False
    if name.isalpha():
        return True
# Validate_age checks wether the learner is within the age bracket required to be able to access and use the learning system.
def validate_age(age):
    if (6<= age<=12):
        return True
# validate_learner_id checks wether the student_id exists within the students.csv file.
def validate_learner_id(student_id,students):
    for student in students:
        if student_id<=0:
                return False
        if student_id==student['student_id']:
            return False
        return True
# validate_menu_choice checks wether the choice selected is within the menu.
def validate_menu_choice(choice):
    if not choice.isdigit():
        return False
    choice=int(choice)
    if  1<=choice<=6:
        return True
    return False

'''Validate_subject checks wether the subject the learner selects is within the provided subjects.If it is not,an error is raised'''
def validate_subject(subject):
    subjects=["mathematics","swahili","English"]
    if subject.strip().title() in subjects:
        return True
    return False

# Validate_answer checks wether the answer selected is correct and also if the learner provided an answer.
def validate_answer(answer):
    if answer is None:
        return False
    if answer.strip()=="":
        return False
    return True