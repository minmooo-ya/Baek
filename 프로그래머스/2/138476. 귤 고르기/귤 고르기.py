# 1. 빈도수 계산
# 2. 빈도 기준 내림차순 정렬
# 3. 하나씩 고르며 k 이상이 될 때까지 누적함
# 4. 종류 수 카운트하여 반환
from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    count = sorted(count.values(), reverse=True)
    
    answer = 0
    total = 0
    
    for c in count:
        total += c
        answer += 1
        if total >= k:
            break
    return answer