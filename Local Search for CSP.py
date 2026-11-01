import random

exams = ['Maths', 'Physics', 'Chemistry', 'English']

conflicts = [
    ('Maths', 'Physics'),
    ('Physics', 'Chemistry'),
    ('Maths', 'English')
]

slots = [1, 2, 3]

result = {}

for exam in exams:
    result[exam] = random.choice(slots)

for i in range(100):
    count = 0

    for a, b in conflicts:
        if result[a] == result[b]:
            count += 1

    if count == 0:
        break

    exam = random.choice(exams)
    result[exam] = random.choice(slots)

print("Exam Timetable:")
print(result)

print("Conflicts:", count)