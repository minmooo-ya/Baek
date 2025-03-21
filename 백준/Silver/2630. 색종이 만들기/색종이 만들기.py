import sys
input = sys.stdin.readline

white_count = 0
blue_count = 0

def paper(x, y, size):
    global white_count, blue_count

    # 현재 영역의 첫 번째 값
    first_value = paper_list[x][y]

    # 현재 영역이 모두 같은 색인지 확인
    is_same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper_list[i][j] != first_value:
                is_same = False
                break
        if not is_same:
            break

    # 모두 같은 색이라면 해당 색 카운트 증가 후 종료
    if is_same:
        if first_value == 0:
            white_count += 1
        else:
            blue_count += 1
        return
    
    # 섞여 있으면 4등분하거 재귀 호출
    mid = size // 2
    paper(x, y + mid, mid)  # 1사분면
    paper(x, y, mid)  # 2사분면
    paper(x + mid, y, mid)  # 3사분면
    paper(x + mid, y + mid, mid)  # 4사분면

# 입력 처리
N = int(input().strip())
paper_list = [list(map(int, input().split())) for _ in range(N)]

# 분할 정복 시작
paper(0, 0, N)

# 결과 출력
print(white_count)
print(blue_count)
