a = 1000 - int(input())   #1000 - 400 = 600
b = [500,100,50,10,5,1]
result = []   # 1,

for i in b:
    if a//i >= 1:          #600//500
        result.append(a//i)       #1
        a = a % i
print(sum(result))
