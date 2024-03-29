word = input()
alphabet = [-1] * 26
word = word.lower()
for i in range(0, len(word)):
    if alphabet[ord(word[i]) - 97] == -1:
        alphabet[ord(word[i]) - 97] = i
print(' '.join(map(str, alphabet)))