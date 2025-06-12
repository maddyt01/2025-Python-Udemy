import pytest
import udemyCourseProject1
#from udemyCourse import grade_calculator

#built in python testing
def test_caclulate_grade_A():
    result = udemyCourseProject1.calculate_grade(100, 95, "Sylvia")
    assert result == "Sylvia scored 95 out of 100 (95.00%) and received a grade of A."

def test_caclulate_grade_B():
    result = udemyCourseProject1.calculate_grade(100, 85, "Brenda")
    assert result == "Brenda scored 85 out of 100 (85.00%) and received a grade of B."

def test_caclulate_grade_C():
    result = udemyCourseProject1.calculate_grade(100, 75, "Carl")
    assert result == "Carl scored 75 out of 100 (75.00%) and received a grade of C."

def test_caclulate_grade_D():
    result = udemyCourseProject1.calculate_grade(100, 65, "David")
    assert result == "David scored 65 out of 100 (65.00%) and received a grade of D."

def test_caclulate_grade_F():
    result = udemyCourseProject1.calculate_grade(100, 55, "Faye")
    assert result == "Faye scored 55 out of 100 (55.00%) and received a grade of F."

# Using pytest to parametrize the tests for different student scores and expected results
@pytest.mark.parametrize("points_possible, score, student_name, expected", [
    (100, 95, "Sylvia", "Sylvia scored 95 out of 100 (95.00%) and received a grade of A."),
    (100, 85, "Brenda", "Brenda scored 85 out of 100 (85.00%) and received a grade of B."),
    (100, 75, "Carl",   "Carl scored 75 out of 100 (75.00%) and received a grade of C."),
    (100, 65, "David",  "David scored 65 out of 100 (65.00%) and received a grade of D."),
    (100, 55, "Faye",   "Faye scored 55 out of 100 (55.00%) and received a grade of F."),
])
def test_calculate_grade(points_possible, score, student_name, expected):
    result = udemyCourseProject1.calculate_grade(points_possible, score, student_name)
    assert result == expected
   