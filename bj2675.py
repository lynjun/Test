n = int(input())

for i in range(n):
    x,y = input().split()
    text = ''
    for j in y:
        text += int(x) * j
    print(text)
