while True:
    a,b,c = map(int,input().split())
    if a*b*c == 0:
        break
    if c>b and c>a:
        if a**2 + b**2 == c**2:
            print('right')
        else:
            print('wrong')
    if b>c and b>a:
        if a**2 + c**2 == b**2:
            print('right')
        else:
            print('wrong')
    if a>c and a>b:
        if b**2 + c**2 == a**2:
            print('right')
        else:
            print('wrong')