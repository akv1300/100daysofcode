student_scores = {
    "Harry" : 82,
    "Ron" : 78,
    'Hermoine' :99,
    "Draco" : 74,
    "Neville" : 62}
studen_grade ={}
for student in student_scores:
    kid = student_scores[student]
    if kid in range (91, 101):
        studen_grade[student] = "Outstanding"
    elif student_scores[student] in range(80,91):
        studen_grade[student] ="Exceeds Expectations"
    elif student_scores[student] in range(70,81):
        studen_grade[student] ="Acceptable"
    else:
        studen_grade[student  ] =("Fail")
print(studen_grade )