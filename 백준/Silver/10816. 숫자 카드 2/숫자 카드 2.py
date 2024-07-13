import sys

M = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

N = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

count_card = {}
for n in a:
    if n in count_card:
        count_card[n] += 1
    else:
        count_card[n] = 1
            
for m in b:
    if m in count_card:
        print(count_card[m], end=' ')
    else:
        print(0, end=' ')