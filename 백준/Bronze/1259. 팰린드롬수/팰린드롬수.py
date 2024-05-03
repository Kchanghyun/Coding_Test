while True:
    a = int(input())
    if a == 0:
        break
    a = list(str(a))
    b = list(reversed(a))
    if a == b:
        print('yes')
    else:
        print('no')
