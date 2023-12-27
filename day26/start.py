import random
import pandas as pd

numbers = [1,2,3]
new_list = [n+1 for n in numbers]
# print(new_list)
double_range = [i*2 for i in range(1,5)]
# print(double_range)
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [n.upper() for n in names if len(n) > 5]
# print(long_names)

student_score = {
    n:random.randint(1,100) for n in names
}
print(student_score)

passed_student = {student:score for (student, score) in student_score.items() if score > 60}
print(passed_student)


student_scores = {
    "student":["Angela", "James", "Lily"]
    , "score":[56, 76, 96]
}

student_df = pd.DataFrame(student_scores)

# Loop through data frame
for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)