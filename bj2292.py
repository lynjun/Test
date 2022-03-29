b = int(input())  # 가야할 방   ->13
n = 1
a = 6             # 규칙
num = 0           # 규칙

while True:            # 1 > 10
    n = n + a * num       # 1. n = 1 + 6 * 0 = 1 / 2. n = 1 + 6 * 1 = 7 / 3. n = 7 + 6 * 3 = 37

    if n >= b:
        break
    num += 1

print(num+1)