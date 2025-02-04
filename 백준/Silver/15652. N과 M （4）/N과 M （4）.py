import sys

n, m = map(int, sys.stdin.readline().split())
s = []

def dfs(a):
    if len(s) == m:
        print(*s)
        return
    
    for i in range(a, n+1):
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)