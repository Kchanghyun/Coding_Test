import sys

n = int(sys.stdin.readline())

a = {}
# 4 * 10000000 = 40000000 = 40000k = 40Mb
# n의 개수가 10,000,000개니까 40mb임.
# 근데 수는 10000보다 작거나 같은 자연수이니까 a = [] * 10000으로 선언해도 될듯
# 그러면 4 * 10000 = 40000 = 40kb 나오네

for i in range(n):
    x= int(sys.stdin.readline())

    if x in a:
        a[x] += 1
    else:
        a[x] = 1

sorted_a = {key : a[key] for key in sorted(a)}

for key, value in sorted_a.items():
    for i in range(value):
        print(key)