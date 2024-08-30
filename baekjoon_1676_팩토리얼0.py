def factorial(x):
    if x == 0:
        return 1
    result = 1
    for i in range(2,x+1):
        result *= i
    return result

def counter(n):
    str_fact = str(factorial(n))
    length = len(str_fact)
    count = 0
    i = length - 1
    while (i >= 0 and str_fact[i] == '0'):
        count += 1
        i -= 1
    return count

n = int(input())
print(counter(n))