n = int(input())
count = 0
for i in range(n):
    group_word = 0
    word = input()
    cnt = []
    for j in range(len(word)):
        string = word[j]
        if string not in cnt:
            cnt.append(string)
        if string in cnt and cnt[len(cnt)-1] != string:
            group_word = 1
    if group_word == 0:
        count += 1
print(count)