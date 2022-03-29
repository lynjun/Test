x ,y = map(int,input().split())

month = [1,3,5,7,8,10,12]
month1 = [4,6,9,11]
month2 = [2]

week = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]

day = 0

for i in range(1,x):
    if i in month:
        day+=31
    elif i in month1:
        day+=30
    elif i in month2:
        day += 28
day += y

day = day % 7

print(week[day])
