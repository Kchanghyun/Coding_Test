n = int(input())
a = list(map(int ,input().split()))
cnt = 0
for i in a:
    prime = True
    if i == 1:
        continue
    for j in range(2, i+1):

        if i%j == 0 and i // j != 1:
            prime = False
            break
    else:
        cnt+=1
print(cnt)
