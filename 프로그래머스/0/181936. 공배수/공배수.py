def solution(number, n, m):
    # answer = 0
    # for x in range(2,50):
    #     for y in range(2, 50):
    #         if (number == n * x and number == m * y):
    #             answer = 1
    # if answer != 1:
    #     answer = 0
    # return answer
    return 0 if number%n or number%m else 1