import sys
N = int(sys.stdin.readline())

data = []
count = dict()
_sum = 0
for i in range(N):
    x = int(sys.stdin.readline())
    data.append(x)

    _sum += x

    if x not in count:
        count[x] = 1
    else:
        count[x] += 1
    
data.sort()

# 산술평균
print(round(_sum / N))

# 중앙값
print(data[len(data) // 2])

# 최빈값
freq = max(count.values())
numbers = []
for key, value in count.items():
    if freq == value:
        numbers.append(key)

numbers.sort()

if len(numbers) == 1:
    print(numbers[0])
else:
    print(numbers[1])

# 범위
print(data[len(data) - 1] - data[0])