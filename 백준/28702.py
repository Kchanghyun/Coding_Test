# 3의 배수 and 5의 배수 = 'FizzBuzz'
# 3의 배수 and !5의 배수 = 'Fizz'
# !3의 배수 and 5의 배수 = 'Buzz'
# !3의 배수 and !5의 배수 = i
import sys

num = 0
for i in range(3):
    x = sys.stdin.readline().strip()
    if x == 'FizzBuzz' or x == 'Fizz' or x == 'Buzz' or num != 0:
        continue
    else:
        try:
            num = int(x) + (3-i)
        except ValueError:
            print('Invalid input, Please enter a valid number or one of the specified strings.')
            sys.exit(1)

if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0 and num % 5 != 0:
    print('Fizz')
elif num % 3 != 0 and num % 5 == 0:
    print('Buzz')
else:
    print(num)


# num % 3 == 0 and num % 5 == 0 -> FizzBuzz
# num % 3 == 0 and num % 5 != 0 -> Fizz
# num % 3 != 0 and num % 5 == 0 -> Buzz
# num % 3 != 0 and num % 5 != 0 -> i