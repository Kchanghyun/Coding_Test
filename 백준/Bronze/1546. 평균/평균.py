N = int(input())
a = list(map(int, input().split()))
avg = 0
original_max = max(a)
for i in range(0, N):
    a[i] = a[i] / original_max * 100
    avg += a[i]
    
print(avg / N)