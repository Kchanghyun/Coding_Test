import sys
n = int(sys.stdin.readline()) # 참가자 수
# 사이즈 별 티셔츠 신청자 수가 들어갈 배열
t_shirts = list(map(int, sys.stdin.readline().split())) 
# 한 사이즈 당 t개의 단위로 주문해야함. ( 몇 묶음을 주문해야 하는 지 계산 )
# p개의 묶음을 주문함. (한개의 묶음 안에 몇개가 들어가는지 계산 + 낱개로 몇개 주문해야하는지 계산)
t, p = map(int, sys.stdin.readline().split())

count_t_shirt = 0

for i in t_shirts:
    x = i // t
    if x >= 1 and i % t == 0: # 묶음 단위가 딱 맞아떨어질 때
        count_t_shirt += (x)
    elif i == 0: # 어떤 사이즈의 신청자가 0일 경우의 수를 배제하고 있었네. 그래서 틀렸네
        continue
    else:
        count_t_shirt += (x+1)

bundle_pen = n // p
each_pen = n % p

print(count_t_shirt)
print(bundle_pen, each_pen)