import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)


best = max(students, key=lambda x: x["grade"])

worst = None

average = None

# 5. Natijani chiqarish
print(f"Eng yaxshi talaba: {best['name']} — {best['grade']}")
print(f"Eng past baho: {worst['name']} — {worst['grade']}")
print(f"O'rtacha baho: {average}")