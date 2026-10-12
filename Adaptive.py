# adaptive.py
# Responsible for rule-based adaptive learning

#Analyzes students' performance using data from the JSON FILE(Rules.json)
from storage import  read_csv_data

import json
def load_rules():
    try:
        with open("Rules.json","r")as file:
            rules=json.load(file)
    except FileNotFoundError:
        print("Rules.json file does not exist.Try again!")
    else:
        return rules
def analyze_performance( student_performance):
    rules=load_rules()
    percentage=student_performance["percentage"]
    if percentage>=rules["performance_rules"]["Excellent"]:
        return "Excellent"
    elif percentage>=rules["performance_rules"]["Good"]:
        return "Good"
    elif percentage>=rules["performance_rules"]["Kudos"]:
        return "Kudos"
    elif percentage>=rules["performance_rules"]["Fair"]:
        return "Fair"
    else:
        return "Poor"


def identify_weak_topic(student_performance):
    if (student_performance["score"])*100<50:
        return student_performance["subject"]


def identify_strong_topic(student_performance):
    if (student_performance["score"])*100>=70:
        return student_performance["subject"]


def recommend_difficulty(student_performance):
    rules=load_rules()
    if (student_performance["score"])*100>=rules["Reviews"]["Excellent"]:
        return (f"Difficulty level: {rules['Reviews']['Excellent']}")
    elif (student_performance["score"])*100>=rules["Reviews"]["Good"]:
        return (f"Difficulty level: {rules['Reviews']['Good']}")
    elif (student_performance["score"])*100>=rules["Reviews"]["Kudos"]:
        return (f"Difficulty level: {rules['Reviews']['Kudos']}")
    elif (student_performance["score"])*100>=rules['Reviews']["Fair"]:
        return (f"Difficulty level: {rules['Reviews']['Fair']}")
    else:
        return (f"Difficulty level: {rules['Reviews']['Poor']}")

def recommend_next_activity(learner_performance,recommended_difficulty,activities):
    for activity in activities:
        if activity["difficulty"] == recommended_difficulty:
            return activity

    return "No suitable activity found."
