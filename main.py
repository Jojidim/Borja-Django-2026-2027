names = ["Ana", "Ben", "Cara", "Dan", "Ella"]

quiz_scores = [
    [85, 90, 78],
    [60, 55, 70],
    [92, 88, 95],
    [45, 50, 40],
    [75, 80, 70],
]

exam_scores = [88, 58, 94, 50, 72]

QUIZ_WEIGHT = 0.40
EXAM_WEIGHT = 0.60
PASSING_GRADE = 60


def compute_quiz_average(scores):
    if len(scores) == 0:
        return 0

    total = 0
    count = 0
    for score in scores:
        total = total + score
        count = count + 1

    average = total / count
    return average

def compute_final_grades(names, quizzes, exams):
    results = []
    for name, scores, exam in zip(names, quizzes, exams):
        quiz_avg = compute_quiz_average(scores)
        weighted_quiz = quiz_avg * QUIZ_WEIGHT
        weighted_exam = exam * EXAM_WEIGHT
        final_grade = round(weighted_quiz + weighted_exam, 2)

        student_result = (name, final_grade)
        results.append(student_result)

    return results

def print_rankings(results):
    sorted_results = sorted([(grade, name) for name, grade in results], reverse=True)

    for rank, (grade, name) in enumerate(sorted_results, start=1):
        print(f"{rank}. {name} - {grade}")


def main():
    results = compute_final_grades(names, quiz_scores, exam_scores)

    print("FINAL GRADES:")
    for name, final_grade in results:
        print(f"{name}: {final_grade}")

    print("RANKNGS:")
    print_rankings(results)

if __name__ == "__main__":
    main()
