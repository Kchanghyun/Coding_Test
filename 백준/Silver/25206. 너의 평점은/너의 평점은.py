n = 20
grade = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
ret = 0.0
rating = 0.0
for i in range(n):
    score = input().split()
    if score[len(score)-1] == 'P':
        n -= 1
        continue
    ret += float(score[1])
    rating += grade[score[2]] * float(score[1])

print(rating/ret)
