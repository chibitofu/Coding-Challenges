## Take in an array of grades 0 - 100
## Round up to the nearest 5, 3 = 5, 2 = 2
## Anything under 38 is left alone
## Returns a array of ints with rounded grades

def round_grades(grades):
    rounded_grades = []

    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            grade_int = grade%10
            new_grade = 0
            if grade_int > 7:
                new_grade = grade + (10 - grade_int)
            elif grade_int >= 5:
                new_grade = grade
            elif grade_int >= 3:
                new_grade = int(round(grade/10) * 10 + 5)
            else:
                new_grade = grade

            rounded_grades.append(new_grade)
    return rounded_grades

test_grades = [73, 67, 40, 33, 84, 99, 100, 81, 82, 83, 85, 86, 87, 88, 89]

print(round_grades(test_grades))

                