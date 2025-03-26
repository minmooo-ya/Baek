import bisect

def count_animals(M, N, L, M_list, animals):
    M_list.sort()
    
    count = 0
    
    for animal in animals:
        animal_x, animal_y = animal
        # 동물의 위치에서 가까운 사대를 찾기 위해 이진 탐색을 사용
        # bisect_left: 동물의 x좌표가 들어갈 위치를 찾음
        idx = bisect.bisect_left(M_list, animal_x)
        
        # 두 개의 사대 후보를 확인
        possible = False
        
        # 사대 후보가 있을 경우
        if idx < M:
            # 오른쪽 사대
            fort_x = M_list[idx]
            if abs(fort_x - animal_x) + animal_y <= L:
                possible = True
        
        if not possible and idx > 0:
            # 왼쪽 사대
            fort_x = M_list[idx - 1]
            if abs(fort_x - animal_x) + animal_y <= L:
                possible = True
        
        # 가능한 경우
        if possible:
            count += 1
    
    return count

M, N, L = map(int, input().split())  
M_list = list(map(int, input().split()))  # 사대의 x좌표
animals = [tuple(map(int, input().split())) for _ in range(N)]  # 동물의 (x, y) 좌표


print(count_animals(M, N, L, M_list, animals))
