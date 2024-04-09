n = int(input())
for i in range(n):
    prev = 0
    ret = 0
    score = input()
    for j in score:
        if j == 'X':
            prev = 0
        else:
            prev += 1
            ret += prev
    print(ret)