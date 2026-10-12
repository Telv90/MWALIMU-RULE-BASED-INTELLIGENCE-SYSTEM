# alphabet.py
# Responsible for alphabet learning activities


def get_alphabet_questions(questions):
    english_questions=[]
    for question in questions:
        if question["subject"].strip().title()=="English":
            english_questions.append(question)
        return english_questions


def select_alphabet_question(questions):
    question=get_alphabet_questions(questions)
    if not question:
        return None
    return question[0]


def present_alphabet_question(question):
    print(f"Question: {question['question']}")
    print(f"Options:")
    for option in question['options']:
        print(f" {option}")


def check_alphabet_answer(user_answer, answer):
    if user_answer.strip().title() == answer.strip().title():
        return True
    return False


def run_alphabet_activity(questions):
    question=select_alphabet_question(questions)
    if question is None:
        print("No alphabet questions found.")
        return
    present_alphabet_question(question)
    user_answer=input("Enter an answer: ")
    score=0
    total_questions=1
    if check_alphabet_answer(user_answer, question['answer']):
        print("Correct answer!")
        score+=1
    else:
        print("Incorrect.Try again!")
    return {
        "score": score,
        "total_questions": total_questions
    }