import sys

def solve():
    s = sys.stdin.readline().strip()
    stack = []
    result = 0
    
    for i in range(len(s)):
        if s[i] == '(':  # 열린 괄호는 스택에 넣기
            stack.append('(')
        else:  # 닫힌 괄호일 때
            stack.pop()
            if s[i - 1] == '(':  # 바로 앞에 열린 괄호가 있으면 레이저
                result += len(stack)  # 레이저가 잘라낸 철사 조각 개수
            else:  # 괄호가 제대로 닫히면 하나의 철사 조각이 완성됨
                result += 1
    
    print(result)

solve()
