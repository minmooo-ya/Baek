import sys
input = sys.stdin.readline

def power(A, B, C):  
    if B == 0: 
        return 1 
    
    half = power(A, B // 2, C)
    
    if B % 2 == 0:  
        return (half * half) % C  # 짝수일 때 (A^(B//2))^2
    else:  
        return (half * half * A) % C  # 홀수일 때 (A^(B//2))^2 * A

A, B, C = map(int, input().split())  
print(power(A, B, C))  
