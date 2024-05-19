m, n = map(int, input().split())

for i in range(m, n+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else: # 위의 for문이 break 없이 끝났다면 (즉, i가 소수라면)
        print(i)