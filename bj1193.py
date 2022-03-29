X = int(input())       # 7

line = 1
while X > line:   #  8 > 1           7>2                 5>3              2>4/ 7 > 1       6>2          4>3         1>4
    X = X - line  # 1. 8 - 1 = 7    2. 7 - 2 = 5        2                    / 7 - 1 = 6   6 - 2 = 4    4 - 3 = 1
    line = line + 1  #  1 + 1 = 2    2 + 1 = 3          4                    / 2           3            4

if line % 2 == 0:
    a = X    #2
    b = line - X + 1  #4 - 2 + 1 =3
else:
    a = line - X + 1      # 3 - 5
    b = X                 #

print(a, '/', b, sep='')    #    1 / 4