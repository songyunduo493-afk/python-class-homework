# Exam Review Priority Calculator
# Course: Intro to Programming
# Function: Calculate review priority based on exam weight & mastery level
def calculate_review_priority(subject_name, exam_weight, mastery_score):
    """
    exam_weight: 0~100, total score proportion of this course
    mastery_score: 0~10, how well you master this subject
    return priority level: High / Medium / Low
    """
    score = exam_weight * (10 - mastery_score)
    if score >= 400:
        return "High Priority — Review first"
    elif score >= 200:
        return "Medium Priority — Arrange daily fixed time"
    else:
        return "Low Priority — Quick review before exam"

# Test sample subjects
if __name__ == "__main__":
    subject_list = [
        ("Accounting", 70, 3),
        ("Calculus", 60, 5),
        ("English", 40, 8)
    ]
    for name, weight, mastery in subject_list:
        res = calculate_review_priority(name, weight, mastery)
        print(f"Subject: {name}, Review Suggestion: {res}")