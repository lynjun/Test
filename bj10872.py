def f(n):
    result = 1
    if n > 0:
        result = n * f(n-1)
    return result
n = int(input())
print(f(n))
