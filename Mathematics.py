# mathematics.py
# Responsible for mathematics learning activities


def get_math_questions(questions):
    math_questions=[]
    for question in questions:
        if question["subject"].title()=="Mathematics":
            math_questions.append(question)
    return math_questions
def select_math_question(questions):
    question=get_math_questions(questions)
    if not question:
        return None
    return question[0] # Return the first question for simplicity.
def present_math_question(question):
    print(f"Question: {question['question']}")
    print("Options:")
    for option in question['options']:
        print(f"  {option}") 
def check_math_answer(user_answer,answer):
    try:
        user_answer = user_answer
    except ValueError:
        return False

    return user_answer == answer
def run_math_activity(questions):
    question=select_math_question(questions)
    if question is None:
        print("No mathematics questions found.")
        return
    present_math_question(question)
    user_answer=input("Enter an answer: ")
    score=0
    total_questions=1
    if check_math_answer(user_answer, question['answer']):
        print("Correct answer!")
        score+=1
    else:
        print("Incorrect.Try again!")
    return {
        "score": score,
        "total_questions": total_questions
    }