n, m = map(int, input().split())
card = list(map(int, input().split()))
ret = 0
for i in card:
    for j in card:
        for k in card:
            if i + j + k > m:
                continue
            if k != i and k != j and i != j:
                if ret < i + j + k:
                    ret = i + j + k
    if ret == m:
        break
print(ret)