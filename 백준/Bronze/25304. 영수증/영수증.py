result = int(input())
N = int(input())
sum = 0
for i in range(1, N+1):
    price, n = map(int, input().split())
    sum = sum + (price * n)
if result == sum:
    print("Yes")
else:
    print("No")