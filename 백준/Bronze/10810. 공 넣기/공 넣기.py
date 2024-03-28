N, M = map(int, input().split())
a = [0]*N
for i in range(0, M):
    q, w, e = map(int, input().split())
    for j in range(q-1, w):
        a[j] = e
print(' '.join(map(str, a)))