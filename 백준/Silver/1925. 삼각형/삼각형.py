#일단 일직선 판정
#좌표ㅕ간 거리 구하고 정삼각형 판정하고 제일 긴 길이를 c로 둘거니까 정렬
#이등변 판정하고 피타고라스 분기 타고 하면 될 듯
#어차피 예둔직은 공통이니까 얘도 분기 
import sys
input = sys.stdin.readline
x1, y1 = map(int, input().strip().split())
x2, y2 = map(int, input().strip().split())
x3, y3 = map(int, input().strip().split())
cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
#일직선 판정(삼각형이 아님)
if cross == 0:
    print("X")
    exit()

d1 = (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)
d2 = (x2 - x3)*(x2 - x3) + (y2 - y3)*(y2 - y3)
d3 = (x3 - x1)*(x3 - x1) + (y3 - y1)*(y3 - y1)

if d1 == d2 == d3:
    print("JungTriangle")
    exit()

a, b, c = sorted([d1, d2, d3])
#이등변 판정
isosceles = (d1 == d2) or (d2 == d3) or (d3 == d1)
#피타고라스 정리
if c == a + b:
    angle = "Jikkak"
elif c > a + b:
    angle = "Dunkak"
else:
    angle = "Yeahkak"

if isosceles:
    print(angle + "2Triangle")
else:
    print(angle + "Triangle")