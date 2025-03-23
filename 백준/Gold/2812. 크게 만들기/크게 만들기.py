import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = input()
num_list = list(num)
stack= []
count = 0  

for num in num_list:

    while stack and count < K and stack[-1] < num:
        stack.pop()
        count += 1
    stack.append(num)

# N-K개의 숫자만 출력
result = ''.join(stack[:N-K])
print(result)
