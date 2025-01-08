import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = {}
    for i in range(n):
        c_name, c_type = sys.stdin.readline().split()

        if c_type not in clothes:
            clothes[c_type] = [c_name]
        else:
            clothes[c_type].append(c_name)
    
    cnt = 1

    # +1을 해준 이유 - 그 종류의 의상을 착용해도 되고 안해도 되기 때문
    # -1을 해준 이유 - 모든 의상을 착용하지 않은 경우를 제외시켜야 하기 대문
    for x in clothes:
        cnt *= (len(clothes[x]) + 1)

    print(cnt - 1)