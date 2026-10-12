
# main.py
# Main controller for Mwalimu AI

from Learners import register_learner
from assessment import generate_assessment_result
from Adaptive import analyze_performance
import json


def display_welcome():
    print("**** WELCOME TO MWALIMU RULE-BASED INTELLIGENT LEARNING SYSTEM ****")
    print(
        "Mwalimu is a system designed to aid junior learners "
        "to understand and learn basic concepts in Mathematics, English and Swahili."
    )


def display_main_menu():
    print("\n**** MAIN MENU ****")
    print("1. Register a learner")
    print("2. Select a subject")
    print("3. Start a learning session")
    print("4. Display assessment results")
    print("5. Display recommendations")
    print("6. Exit")


def register_new_learner():
    learner = register_learner()

    if learner:
        print("Learner registered successfully ")

    return learner


def select_subject():
    choice = input(
        "Select a subject:\n"
        "1. Mathematics\n"
        "2. English\n"
        "3. Swahili\n"
    )

    if choice in ["1", "2", "3"]:
        return choice

    print("Invalid input. Try again.")
    return None


def load_questions():
    try:
        with open("questions.json", "r") as file:
            questions = json.load(file)

    except FileNotFoundError:
        print("questions.json file does not exist.")
        return []

    except json.JSONDecodeError:
        print("questions.json contains invalid JSON.")
        return []
    else:
        return questions


def start_learning_session(learner, subject, questions):

    if subject == "1":
        from Mathematics import run_math_activity
        return run_math_activity(questions)

    elif subject == "2":
        from English import run_alphabet_activity
        return run_alphabet_activity(questions)

    elif subject == "3":
        from Swahili import run_swahili_activity
        return run_swahili_activity(questions)

    else:
        print("Invalid input. Please select an appropriate subject.")
        return None


def display_results(performance_rules):
    print("\n**** ASSESSMENT RESULTS ****")
    print(f"Total Assessment Score: {performance_rules['score']}")
    print(f"Total Questions: {performance_rules['total_questions']}")
    print(f"Percentage: {performance_rules['percentage']}%")
    print(f"Performance Level: {performance_rules['performance_level']}")


def display_recommendation(recommendation):
    print("\n**** LEARNING RECOMMENDATION ****")
    print(f"Recommendation: {recommendation}")


def main():

    display_welcome()

    learner = None
    subject = None
    questions = []
    assessment_score = None
    recommendation = None

    while True:

        display_main_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            learner = register_new_learner()

        elif choice == "2":

            subject = select_subject()

        elif choice == "3":

            if learner is None:
                print("Please register a learner first.")
                continue

            if subject is None:
                print("Please select a subject first.")
                continue

            questions = load_questions()

            if not questions:
                print("No questions available.")
                continue

            activity_result = start_learning_session(
                learner,
                subject,
                questions
            )

            if activity_result is not None:

                score = activity_result["score"]
                total_questions = activity_result["total_questions"]

                performance_rules = generate_assessment_result(
                    score,
                    total_questions
                )

                recommendation = analyze_performance(
                    performance_rules
                )

                print("\nLearning session completed.")

        elif choice == "4":

            if assessment_score is not None:
                display_results(performance_rules)
            else:
                print("No assessment results to display.")

        elif choice == "5":

            if recommendation is not None:
                display_recommendation(recommendation)
            else:
                print("No recommendations available.")

        elif choice == "6":

            print("Thank you for using Mwalimu!")
            break

        else:

            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
