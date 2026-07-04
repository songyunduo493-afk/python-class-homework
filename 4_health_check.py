# Exam Preparation Health Check Tool
# Function: Judge whether your rest & study status is healthy
def health_check(sleep_hour, continuous_study_hour, exercise_min):
    warning_msg = []
    if sleep_hour < 6:
        warning_msg.append("Warning: Sleep less than 6 hours, will reduce memory efficiency")
    if continuous_study_hour > 3:
        warning_msg.append("Warning: Continuous study over 3 hours, brain fatigue risk")
    if exercise_min < 20:
        warning_msg.append("Warning: Lack of exercise, poor mental state")
    if len(warning_msg) == 0:
        warning_msg.append("Excellent study & rest balance, high exam efficiency!")
    return warning_msg

if __name__ == "__main__":
    # Input your daily status data
    sleep = 5.5
    long_study = 3.5
    exercise = 15
    result = health_check(sleep, long_study, exercise)
    print("=== Exam Health Status Report ===")
    for tip in result:
        print(tip)