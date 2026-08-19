import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)


best = max(students, key=lambda x: x["grade"])

worst = min(students, key=lambda x: x["grade"])

total_students = len(students)
total_scores = 0
for student in students:
        total_scores += student["grade"]

average = round(total_scores/total_students, 1)


print(f"Eng yaxshi talaba: {best['name']} — {best['grade']}")
print(f"Eng past baho: {worst['name']} — {worst['grade']}")
print(f"O'rtacha baho: {average}")