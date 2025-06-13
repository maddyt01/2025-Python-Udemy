# Project 1 from Nick Walter's "Python for Programmers Course" on udemy
# Grade Calculator
# This project calculates the grade of student "student_name" given their "score" and the total "points_possible"

def calculate_grade(points_possible, score, student_name):
    percentage = (score / points_possible) * 100
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"
    return f"{student_name} scored {score} out of {points_possible} ({percentage:.2f}%) and received a grade of {grade}."

def grade_calculator():
    try:
        points_possible = int(input("Enter total possible points: "))
        print("Valid input for total possible points.")
    except ValueError:
        print("Invalid input for total possible points. Please enter a number.")
        return None
    
    try:
        score = int(input("Enter student score: "))
        print("Valid input for student score.")
    except ValueError:
        print("Invalid input for student score. Please enter a number.")
        return None
    
    student_name = input("Enter student name: ")
    return calculate_grade(points_possible, score, student_name)

#print(grade_calculator())