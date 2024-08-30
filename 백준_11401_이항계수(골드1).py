def factorial(x):
    if x == 0:
        return 1
    result = 1
    for i in range(1,x+1):
        result *= i
        result %= MOD
    return result

# x의 모듈러 역원을 구하는 함수. 큰수의 mod를 빠르게 연산하기 위해 페르마 소정리 사용
def mod_inv(x, mod):
    return pow(x, mod-2, mod) #pow() : x^y, mod 세개의 변수를 매개변수로 받음

def binomial(n,k):
    if k < 0 or k > n:
        return 0
    fact_n = factorial(n)
    fact_n_k = factorial(n-k)
    fact_k = factorial(k)
    # (fact_n * mod_inv(fact_k) * mod_inv(fact_n_k)) % MOD
    # 계산을 빠르게 하기 위해 MOD로 나눈 나머지를 여러차례 계산함(나머지 정리)...나머지는 나머지끼리 계산한다...
    return (fact_n * mod_inv(fact_k, MOD) % MOD * mod_inv(fact_n_k, MOD) % MOD) % MOD

MOD = 1000000007
n, k = map(int, input().split())
print(binomial(n,k))