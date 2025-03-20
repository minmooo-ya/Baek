import sys
input = sys.stdin.readline

def cut_tree(N_list, M):  
    st, en = 0, max(N_list) 

    while st <= en:
        mid = (st + en) // 2  
        cut_sum = sum(tree - mid for tree in N_list if tree > mid)  # 잘린 나무 총합 계산

        if cut_sum < M:  # 필요한 양보다 적음 -> 더 낮게 잘라야 함
            en = mid - 1
        else:  # 필요한 양보다 많음 -> 더 높게 잘라도 됨
            st = mid + 1

    return en  

N, M = map(int, input().split())   
N_list = sorted(map(int, input().split())) 

print(cut_tree(N_list, M))  
