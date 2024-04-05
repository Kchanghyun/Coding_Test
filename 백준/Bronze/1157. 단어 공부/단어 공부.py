word = input()
word = word.lower()
a = [0] * 26
for i in range(len(word)):
    a[ord(word[i]) - 97] += 1
# print(a.index(max(a)))
# max(a)는 가장 큰 값의 첫 번째 인덱스의 값을 반환한다.
duplication = 0
for i in range(0, len(a)):
    if i == a.index(max(a)):
        continue
    if a[i] == max(a):
        duplication = -1

if duplication == -1:
    print("?")
else:
    print(chr(a.index(max(a)) + 65))