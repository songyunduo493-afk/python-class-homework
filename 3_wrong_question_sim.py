# Wrong Question Score Improvement Simulator
# Function: Simulate score growth by reviewing wrong exercises
def score_simulator(original_score, wrong_topic_list):
    point_per_topic = 2.5
    improved_score = original_score
    improved_list = []
    # Traverse all weak topics
    for topic in wrong_topic_list:
        improved_score += point_per_topic
        improved_list.append(f"Master {topic}, +{point_per_topic} points")
    return round(improved_score, 1), improved_list

if __name__ == "__main__":
    base_score = 62
    weak_points = ["Financial Accounting", "Calculus Derivative", "English Reading", "Excel Function"]
    final_score, improve_details = score_simulator(base_score, weak_points)
    print(f"Original exam score: {base_score}")
    print("Score improvement details:")
    for detail in improve_details:
        print("-", detail)
    print(f"Estimated score after reviewing all weak points: {final_score}")