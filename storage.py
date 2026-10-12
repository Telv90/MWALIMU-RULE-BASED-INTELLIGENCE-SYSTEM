# storage.py
# Responsible for JSON and CSV data storage
import csv
import json

def create_data_file(student_id, name, age, subject,question, answer, correct_answer, score,percentage):
    students=[{
        "student_id":student_id,
        "name":name,
        "age":age,
        "subject":subject,
        "question":question,
        "answer":answer,
        "correct_answer":correct_answer,
        "score":score,
        "percentage":percentage
    }]
    try:
        with open("students_performance.csv","x",newline="")as file:
            fieldnames=["student_id","name","age","subject","question","answer","correct_answer","score","percentage"]
            writer=csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
    except FileExistsError:
        print("students_performance.csv file already exists.")
    except Exception as e:
        print(f"Error creating data file: {e}")
    except OSError:
        print("Error occured while creating the file.Please try again")

def load_json_data():
    try:
     with open("questions.json","r")as file:
        questions=json.load(file)
    except FileNotFoundError:
        print("questions.json file not detected yet.Try again")
    return questions

def save_json_data(questions,rules):
    try:
        with open("questions.json","w")as file:
            json.dump(questions,file,indent=4)
    except Exception as e:
        print(f"Error saving JSON data: {e}")
    try:
        with open("Rules.json","w")as file:
            json.dump(rules,file,indent=4)
    except Exception as e:
        print(f"Error saving JSON data: {e}")

def read_csv_data():
    try:
      with open("students_performance.csv","r")as file:
        reader=csv.DictReader(file)
        students=[row for row in reader]
    except FileNotFoundError:
        print("students_performance.csv file not found.Please ensure the file exists.")
    return students
def write_csv_data(students):
    try:
     with open("students_performance.csv","w",newline="")as file:
         fieldnames=["student_id","name","age","subject","question","answer","correct_answer","score"]
         writer=csv.DictWriter(file,fieldnames=fieldnames)
         writer.writeheader()
         writer.writerows(students)
    except FileNotFoundError:
        print("students_performance.csv file not found.Please ensure the file exists.")


def append_performance_record(student):
    new_student={
        "student_id":student['student_id'],
        "name":student['name'],
        "age":student['age'],
        "subject":student['subject'],
        "question":student['question'],
        "answer":student['answer'],
        "correct_answer":student['correct_answer'],
        "score":student['score']
    }
    try:
     with open("students_performance.csv","a+",newline="")as file:
            fieldnames=["student_id","name","age","subject","question","answer","correct_answer","score"]
            writer=csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows([new_student])
    except Exception as e:
        print(f"Error appending performance record: {e}")


def update_json_data(questions):
    try:
        with open("questions.json","a")as file:
            json.dump(questions,file,indent=4)
    except Exception as e:
        print(f"Error updating JSON data: {e}")
    except FileNotFoundError:
        print("questions.json file not detected.Try again")