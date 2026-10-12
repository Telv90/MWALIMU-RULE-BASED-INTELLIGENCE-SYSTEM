# swahili.py
# Responsible for Swahili learning activities


def get_swahili_questions(questions):
    swahili_questions=[]
    for question in questions:
        if question["subject"].strip().title()=="Swahili":
            swahili_questions.append(question)
    return swahili_questions

def select_swahili_question(questions):
    question=get_swahili_questions(questions)
    if not question:
        return None
    return question[0]


def present_swahili_question(question):
    print(f"Question: {question['question']}")
    print(f"Options:")
    for option in question['options']:
        print(f" {option}")

def check_swahili_answer(user_answer,answer):
    if user_answer.strip().title()==answer.strip().title():
        return True
    return False


def run_swahili_activity(questions):
    question=select_swahili_question(questions)
    if question is None:
        print("No Swahili questions found.")
        return
    present_swahili_question(question)
    user_answer=input("Enter an answer: ")
    score=0
    total_questions=1
    if check_swahili_answer(user_answer, question['answer']):
        print("Correct answer!")
        score+=1
    else:
        print("Incorrect.Try again!")
    return {
        "score": score,
        "total_questions": total_questions
    }