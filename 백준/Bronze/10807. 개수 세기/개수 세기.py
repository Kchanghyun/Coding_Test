n = int(input())
#a = []
a = [0] * n
a = list(map(int, input().split()))
count = int(input())

print(a.count(count))