import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
is_answer = False

def dfs(x, y, i):
    global is_answer
    if x*2 <= y:
        dfs(x*2, y, i+1)
    if int(str(x) + '1') <= y:
        dfs(int(str(x) + '1'), y, i+1)

    if x*2 == y or int(str(x) + '1') == y:
        is_answer = True
        print(i+1)
        return


dfs(a, b, 1)
if not is_answer:
    print(-1)