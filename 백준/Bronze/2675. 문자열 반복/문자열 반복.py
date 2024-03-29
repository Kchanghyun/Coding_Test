n = int(input())
for i in range(n):
    count, word = input().split()
    new_word = [] * (len(word) * int(count))
    for j in range(len(word)):
        new_word += word[j] * int(count)
    print(''.join(new_word))
