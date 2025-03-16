import sys

def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]: 
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

def gold(n, primes):
 
    mid = n // 2  
    for i in range(mid, 1, -1): 
        if primes[i] and primes[n - i]:  
            return i, n - i  
    return None  

# 입력 처리
T = int(sys.stdin.readline())  
primes = sieve(10000) 

for _ in range(T):
    n = int(sys.stdin.readline())  
    a, b = gold(n, primes)
    print(a, b)
