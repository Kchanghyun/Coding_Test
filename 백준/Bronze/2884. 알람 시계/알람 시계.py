# time = input()
# hour, minute = time.split()
# hour = int(hour)
# minute = int(minute)

hour, minute = map(int, input().split())

# if 45 <= minute < 60:
#     minute -= 45
# elif 0 <= minute < 45 and 1 < hour < 24:
#     minute += 15
#     hour -= 1
# elif 45 > minute >= 0 >= hour:
#     minute += 15
#     hour = 23

if minute < 45:
    if hour == 0:
        hour = 23
        minute += 60
    elif hour != 0:
        hour -= 1
        minute += 60

print(hour, minute-45)