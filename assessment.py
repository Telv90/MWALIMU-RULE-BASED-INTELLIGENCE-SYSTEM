# assessment.py
# Responsible for evaluating learner performance


def check_answer(user_answer, answer):
    if user_answer.strip().title()==answer.strip().title():
        return True
    return False


def calculate_score(score, total_questions):
    if total_questions == 0:
        return 0
    return score / total_questions

def calculate_percentage(score, total_questions):
    percentage = calculate_score(score, total_questions) * 100
    return percentage


def determine_performance_level(percentages):
    if percentages >=70:
        return "Strong"
    elif 50<=percentages<70:
        return "Fair"
    elif percentages<50:
        return "Weak.Needs improvement"
    else:
        return "Alarmingly low performance. Immediate follow-up required."


def generate_assessment_result(score, total_questions):
    percentage = calculate_percentage(score, total_questions)
    performance_level = determine_performance_level(percentage)
    return {
        "score": score,
        "total_questions": total_questions,
        "percentage": percentage,
        "performance_level": performance_level
    }


def summarize_performance(score, total_questions, question=None):
    percentage = calculate_percentage(score, total_questions)
    performance_level = determine_performance_level(percentage)
    print("****Assessment Summary report****")
    print(f"Total Marks: {score}/{total_questions}")
    print(f"Learner's Performance Level:{performance_level}")
    print(f"Percentage: {percentage:.2f}%")
    print("**********************************")