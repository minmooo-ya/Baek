def solution(s):
    answer = ''
    numbers = list(map(int, s.split()))
    mn = min(numbers)
    mx = max(numbers)
    answer = f"{mn} {mx}"
    return answer