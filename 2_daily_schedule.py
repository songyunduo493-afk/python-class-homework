# Daily Exam Review Schedule Timer
# Function: Generate balanced daily study schedule for final exam
def generate_study_plan(total_study_hours, subject_count):
    plan = []
    single_subject_hour = round(total_study_hours / subject_count, 1)
    # Loop to create schedule for each subject
    for day in range(1, 8):
        daily_arrange = f"Day{day}: Each subject studies {single_subject_hour} hours, take 10 mins break per hour"
        plan.append(daily_arrange)
    return plan

if __name__ == "__main__":
    # Input your total daily available study time
    daily_hours = 6
    course_num = 4
    week_plan = generate_study_plan(daily_hours, course_num)
    print("=== One Week Exam Review Schedule ===")
    for line in week_plan:
        print(line)