n = int(input())
ret = 666
count = 0
while True:
    if '666' in str(ret):
        count += 1

        if count == n:
            break
    ret += 1

print(ret)