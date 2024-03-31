alphabet = input()
sum = 0
for i in range(len(alphabet)):
    if 'A' <= alphabet[i] <= 'C':
        sum += 3
    elif 'D' <= alphabet[i] <= 'F':
        sum += 4
    elif 'G' <= alphabet[i] <= 'I':
        sum += 5
    elif 'J' <= alphabet[i] <= 'L':
        sum += 6
    elif 'M' <= alphabet[i] <= 'O':
        sum += 7
    elif 'P' <= alphabet[i] <= 'S':
        sum += 8
    elif 'T' <= alphabet[i] <= 'V':
        sum += 9
    else:
        sum += 10
print(sum)