import sys

def my_round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)

n = int(sys.stdin.readline())

arr = []

if n != 0:
    for i in range(n):
        arr.append(int(sys.stdin.readline()))
    arr.sort()
    excepts = my_round(n * 0.15)

    if excepts > 0:
        arr = arr[excepts : -excepts]
    
    ret = my_round(sum(arr) / len(arr))
    print(ret)

else:
    print(0)
    