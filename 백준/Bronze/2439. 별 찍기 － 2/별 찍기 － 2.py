n = int(input())
for i in range(1,n+1):
    s = "%s" % "*"*i
    print(s.rjust(n))