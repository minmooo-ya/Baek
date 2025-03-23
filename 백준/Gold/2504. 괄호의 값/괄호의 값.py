import sys

def VPS2(s):
    stack = []
    temp = 1
    result = 0

    for i, char in enumerate(s):
        if char == '(':
            temp *= 2
            stack.append(char)
        elif char == '[':
            temp *= 3
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return 0
            if s[i - 1] == '(':  # 바로 닫히는 경우
                result += temp
            stack.pop()
            temp //= 2
        elif char == ']':
            if not stack or stack[-1] != '[':
                return 0
            if s[i - 1] == '[':  # 바로 닫히는 경우
                result += temp
            stack.pop()
            temp //= 3

    return result if not stack else 0  # 스택이 남아 있으면 잘못된 입력


s = sys.stdin.readline().strip()
print(VPS2(s))
