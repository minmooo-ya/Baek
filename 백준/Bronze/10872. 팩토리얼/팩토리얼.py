def factorial(N):
    result = 1
    for i in range(2, N + 1):
        result *= i
    print(result)
    return result

N = int(input())
factorial(N)

