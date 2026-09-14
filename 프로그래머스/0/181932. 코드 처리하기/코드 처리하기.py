def solution(code):
    answer = ''
    mode = False
    for i in range(len(code)):
        if code[i] == "1":
            mode = not mode
        elif code[i] != "1":
            if not mode and i%2 == 0:
                answer += code[i]
            elif mode and i%2 == 1:
                answer += code[i]
    if answer == '':
        answer = "EMPTY"
    return answer