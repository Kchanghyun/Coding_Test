word = list(map(str, input()))
reverse_word = list(reversed(word))
if word == reverse_word:
    print(1)
else:
    print(0)