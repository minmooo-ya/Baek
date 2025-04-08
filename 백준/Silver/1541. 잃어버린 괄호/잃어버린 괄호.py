expression = input().strip()

# '-' 기준으로 먼저 나눔
parts = expression.split('-')

# 첫 번째 덩어리는 무조건 더함
total = sum(map(int, parts[0].split('+')))

# 나머지 덩어리는 각각 '+'로 나눈 뒤 전부 빼줌
for part in parts[1:]:
    total -= sum(map(int, part.split('+')))

print(total)
