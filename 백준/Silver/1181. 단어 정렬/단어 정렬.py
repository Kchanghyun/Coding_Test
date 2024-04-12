n = int(input())
words = []
for i in range(n):
    words.append(input())
words = list(set(words))
sorted_words = sorted(words, key=lambda x: (len(x), x))
print(*sorted_words, sep='\n')