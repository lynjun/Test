a,b,c = map(int,input().split())
d = 1  #판매 갯수

if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)