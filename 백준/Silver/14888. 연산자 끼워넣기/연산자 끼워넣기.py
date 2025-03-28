N = int(input())  
N_list = [int(x) for x in input().split()]  
add, sub, mul, div = map(int, input().split())  

max_value = -int(1e9)  
min_value = int(1e9)   

def dfs(curr, data):
    global add, sub, mul, div, max_value, min_value

    # 마지막 수까지 계산이 끝났으면 최댓값과 최솟값 갱신
    if curr == N:
        max_value = max(max_value, data)
        min_value = min(min_value, data)
        return
    
    if add > 0:
        add -= 1
        dfs(curr + 1, data + N_list[curr])  
        add += 1  
    
    if sub > 0:
        sub -= 1
        dfs(curr + 1, data - N_list[curr])  
        sub += 1  

    if mul > 0:
        mul -= 1
        dfs(curr + 1, data * N_list[curr])  
        mul += 1  

    if div > 0:
        div -= 1
        dfs(curr + 1, int(data / N_list[curr]))  # 다음 수로 넘어가며 정수 나눗셈
        div += 1  

dfs(1, N_list[0])

print(max_value)
print(min_value)
