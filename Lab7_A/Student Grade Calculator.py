''' A Python program that uses pre-existing course data to calculate a student's weighted final grade '''


import course_data

student = input("Enter student name: ")

if student not in course_data.data["roster"]:
    print("Student not found")

else:
    student_score = []
    print(f"{student}:\n")

    for assignment_name, assignment in course_data.data["assignments"].items():
        if student not in assignment["submissions"]:
            assignment["submissions"][student] = 0

        student_score.append(assignment["submissions"][student] * assignment["weight"])

        print(f"{assignment_name}: {assignment["submissions"][student]}%")

    final_score = sum(student_score) / 100
    print(f"Total grade: {final_score:.2f}%\n")
