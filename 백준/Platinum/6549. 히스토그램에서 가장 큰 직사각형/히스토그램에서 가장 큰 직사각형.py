import sys

def largest_rectangle(hist):
    stack = []
    max_area = 0
    n = len(hist)

    for i in range(n):
        while stack and hist[stack[-1]] > hist[i]:
            h = hist[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    while stack:
        h = hist[stack.pop()]
        w = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * w)

    return max_area

output_results = []


while True:
    line = sys.stdin.readline().strip()
    if not line:
        continue  # 빈 줄이면 무시하고 계속 진행
    data = list(map(int, line.split()))
    if data[0] == 0:
        break  # 0이 입력되면 종료
    output_results.append(str(largest_rectangle(data[1:])))

sys.stdout.write("\n".join(output_results) + "\n")
