data = []
data1= []
for i in range(1,10000):
    data.append(i)

for i in data:
    if i<10:
        a = i + i%10
        data1.append(a)
    if i >= 10 and i < 99:
        a = i + i//10 + i %10
        data1.append(a)
    if i >= 100 and i <999:
        a = i + i//100 + ((i%100)//10) + ((i%100)%10)
        data1.append(a)
    if i >= 1000 and i <9999:
        a = i + i//1000 + ((i%1000)//100) + (((i%1000)%100)//10) + (((i%1000)%100)%10)
        if a < 10000:
            data1.append(a)

sdata = set(data) ^ set(data1)

for i in sdata:
    print(i)

