x, y = map(int,input().split())
c = int(input())

x_list = [0, x]
y_list = [0, y]

for _ in range(c):
    e, p = map(int, input().split())
    if e == 0:
        y_list.append(p)
    else:
        x_list.append(p)

x_list.sort()
y_list.sort()

max_x = 0
for i in range(len(x_list)):
    g = x_list[i] - x_list[i-1]
    if max_x < g:
        max_x = g
max_y = 0
for i in range(1,len(y_list)):
    g = y_list[i]- y_list[i-1]
    if max_y < g:
        max_y = g

print(max_x*max_y)

