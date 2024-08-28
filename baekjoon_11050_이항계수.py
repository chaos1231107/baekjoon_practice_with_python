def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

def binomial(n,k):
    if k < 0 or k > n:
        return 0
    return int(factorial(n) / (factorial(k) * factorial(n-k)))
n, k = map(int, input().split())
print(binomial(n,k))